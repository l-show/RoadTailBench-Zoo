from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class SensorSpec:
    type: str
    id: str
    transform: Dict[str, float] = field(default_factory=dict)
    attributes: Dict[str, Any] = field(default_factory=dict)


@dataclass
class RTBObservation:
    frame: int
    timestamp: float
    ego_state: Dict[str, Any]
    route: List[List[float]]
    sensors: Dict[str, Any] = field(default_factory=dict)
    actors: List[Dict[str, Any]] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)
    raw: Dict[str, Any] = field(default_factory=dict)


@dataclass
class RTBControl:
    steer: float = 0.0
    throttle: float = 0.0
    brake: float = 0.0
    hand_brake: bool = False
    reverse: bool = False
    target_speed_mps: Optional[float] = None
    diagnostics: Dict[str, Any] = field(default_factory=dict)

    def to_carla(self, carla):
        return carla.VehicleControl(
            steer=float(self.steer),
            throttle=float(self.throttle),
            brake=float(self.brake),
            hand_brake=bool(self.hand_brake),
            reverse=bool(self.reverse),
        )
