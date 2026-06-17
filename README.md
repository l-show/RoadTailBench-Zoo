# RoadTailBench-Zoo

RoadTailBench-Zoo is the model adapter layer for RoadTailBench closed-loop evaluation.

All adapters convert model-specific inputs and outputs into one RoadTailBench protocol:

- input: `RTBObservation`
- output: `RTBControl`

This repository does not vendor Bench2DriveZoo code. VAD, UniAD, Alpamayo, OpenDriveVLA, and other models should be integrated through adapters that import their own upstream repositories from local paths or installed packages.

## Quick Start

```powershell
pip install -e G:\Codex\RoadTailBench-Zoo
```

Use the built-in rule-based adapter:

```powershell
rtb-run ... --ego-mode agent_ego --agent roadtailbench_zoo.adapters.rule_based:RuleBasedAdapter
```

## License Notes

Code in this repository is Apache-2.0. Model checkpoints may have different licenses and are not stored here. Alpamayo public code is Apache-2.0, but its model weights are non-commercial; document the exact upstream terms before distributing configs or results.
