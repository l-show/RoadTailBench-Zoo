# 模型接入状态

## VAD / UniAD

当前只提供外部桥接 stub。不要复制 Bench2DriveZoo 中的 VAD/UniAD agent 代码到本仓库。后续做法是让用户在本地安装或 clone 上游模型仓库，然后在 adapter 中通过配置导入。

## Alpamayo

公开 GitHub 代码采用 Apache-2.0，可以设计 adapter。需要注意模型权重是非商业许可，checkpoint 不进入本仓库。公开结果时必须注明权重许可。

## OpenDriveVLA

当前公开仓库的模型代码、checkpoint 和推理代码仍不完整，因此本仓库先保留 `OpenDriveVLAAdapter` stub。等上游发布完整推理接口后，再实现 sensor preprocessing 和 control postprocess。

## 新模型接入检查表

1. 确认代码许可证。
2. 确认 checkpoint 许可证。
3. 明确模型输入：图像、lidar、BEV、route、语言、历史状态。
4. 明确模型输出：控制、轨迹、速度、语言动作。
5. 在 adapter 中转换为 `RTBControl`。
6. 用 `RuleBasedAdapter` 相同的闭环 runner 验证。
