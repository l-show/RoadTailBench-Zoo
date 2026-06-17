# RoadTailBench-Zoo Adapter Protocol

所有模型最终都适配为同一个闭环接口：

```python
adapter.setup(config)
adapter.sensors()
control = adapter.run_step(observation)
adapter.destroy()
```

`run_step` 输出必须能转换为 CARLA `VehicleControl`：

```text
steer   [-1, 1]
throttle [0, 1]
brake   [0, 1]
```

如果模型原始输出是轨迹、目标点、语言动作或速度规划，adapter 必须在内部转换为 `RTBControl`。转换策略可以是 PID、MPC 或模型自带控制头，但输出协议不能改变。

## 推荐适配层

- perception/model preprocessing：读取相机、lidar、ego state、route、hazard metadata。
- model inference：调用上游模型。
- postprocess：把模型输出转为目标轨迹或控制量。
- control bridge：输出 `RTBControl`。

## 不进入本仓库的内容

- 模型 checkpoint。
- Bench2DriveZoo 顶层 CC BY-NC-ND 代码。
- 未确认许可证的上游模型代码。
