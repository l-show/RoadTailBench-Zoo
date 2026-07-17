# Repository Guidelines

## Role In The Two-Repo Setup

`G:\Codex\RoadTailBench-Zoo` is the model adapter repository. It does not run the benchmark by itself. The benchmark/runtime entry point is `G:\Codex\RoadTailBench`, which owns scenes, metadata, frame logging, and metrics.

Use this repository when adding or modifying adapters for `rtb-run --ego-mode agent_ego --agent <module>:<Class>`.

## Project Structure & Module Organization

- `roadtailbench_zoo/protocol/`: shared adapter protocol, including `BaseAdapter`, `RTBObservation`, `RTBControl`, and sensor specs.
- `roadtailbench_zoo/adapters/`: concrete model adapters such as `rule_based`, `vad`, `uniad`, `alpamayo`, and `opendrivevla`.
- `configs/`: local adapter config examples and stubs.
- `checkpoints/`: local checkpoint placeholder only; do not commit model weights.
- `docs/`: protocol and model status notes.
- `tests/`: smoke tests.

## Build, Test, And Development Commands

- `pip install -e .`: install Zoo adapters in editable mode.
- `pip install -e G:\Codex\RoadTailBench`: install the benchmark runner used to execute adapters.
- `pytest`: run Zoo smoke tests.
- `rtb-run --host localhost --port 2000 --scene-root G:\Codex\RoadTailBench\scenes --metadata-root G:\Codex\RoadTailBench\metadata --scenes RTB116 --ego-mode agent_ego --agent roadtailbench_zoo.adapters.rule_based:RuleBasedAdapter`: test adapter integration from the Bench repository.

## Adapter Contract

Adapters expose:

- `setup(config)`
- `sensors()`
- `run_step(observation)`
- `destroy()`

`run_step` must return an `RTBControl` or an object with `to_carla(carla)`. Final CARLA control values must respect:

- `steer`: `[-1, 1]`
- `throttle`: `[0, 1]`
- `brake`: `[0, 1]`

If an upstream model returns a trajectory, waypoint, language action, target speed, or planner state, the adapter is responsible for converting that output into `RTBControl`.

## Ego Mode Boundary

Zoo adapters assume the Bench runner already spawned the ego in `agent_ego` mode. Do not add scene-spawn suppression logic in Zoo. If a scene still creates its own ego during `agent_ego`, fix that in `G:\Codex\RoadTailBench` by respecting `ROADTAILBENCH_EGO_MODE=agent_ego` in the scene/runtime compatibility path.

## Coding And License Rules

Use Python 3.8+ syntax and four-space indentation. Keep adapters thin around upstream model code and isolate model-specific imports so unavailable optional dependencies do not break unrelated adapters. Do not vendor Bench2DriveZoo code, incompatible-license code, or checkpoints. External model paths should be configured locally through adapter config files or environment variables.
