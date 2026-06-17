from roadtailbench_zoo.protocol import RTBControl
from roadtailbench_zoo.adapters.external_stub import ExternalModelStubAdapter


def test_control_defaults():
    control = RTBControl()
    assert control.steer == 0.0
    assert control.throttle == 0.0
    assert control.brake == 0.0


def test_stub_brakes():
    adapter = ExternalModelStubAdapter()
    adapter.setup({"model_name": "test"})
    control = adapter.run_step({})
    assert control.brake == 1.0
    assert control.diagnostics["reason"] == "adapter_stub"
