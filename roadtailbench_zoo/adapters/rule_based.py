import math

from roadtailbench_zoo.protocol import BaseAdapter, RTBControl


class RuleBasedAdapter(BaseAdapter):
    name = "rule_based"

    def setup(self, config):
        super().setup(config)
        self.target_speed_mps = float(self.config.get("target_speed_mps", 8.0))
        self.k_steer = float(self.config.get("k_steer", 0.8))
        self.k_speed = float(self.config.get("k_speed", 0.25))

    def run_step(self, observation):
        ego = observation.get("ego") if isinstance(observation, dict) else None
        config = observation.get("config", {}) if isinstance(observation, dict) else {}
        if ego is None:
            return RTBControl(brake=1.0, diagnostics={"reason": "missing_ego_actor"})
        route = config.get("centerline_route") or config.get("route") or []
        if not route:
            return RTBControl(throttle=0.2, diagnostics={"reason": "missing_route"})
        loc = ego.get_location()
        tf = ego.get_transform()
        target = None
        for point in route:
            px, py = (point.get("x"), point.get("y")) if isinstance(point, dict) else (point[0], point[1])
            if math.hypot(float(px) - loc.x, float(py) - loc.y) > 5.0:
                target = (float(px), float(py))
                break
        if target is None:
            return RTBControl(brake=1.0, diagnostics={"reason": "route_finished"})
        desired_yaw = math.atan2(target[1] - loc.y, target[0] - loc.x)
        yaw = math.radians(tf.rotation.yaw)
        err = desired_yaw - yaw
        while err > math.pi:
            err -= 2 * math.pi
        while err < -math.pi:
            err += 2 * math.pi
        vel = ego.get_velocity()
        speed = math.sqrt(vel.x * vel.x + vel.y * vel.y + vel.z * vel.z)
        speed_error = self.target_speed_mps - speed
        throttle = max(0.0, min(0.75, speed_error * self.k_speed))
        brake = max(0.0, min(0.8, -speed_error * self.k_speed))
        return RTBControl(
            steer=max(-0.7, min(0.7, err * self.k_steer)),
            throttle=throttle,
            brake=brake,
            target_speed_mps=self.target_speed_mps,
            diagnostics={"target": target, "speed_mps": speed},
        )
