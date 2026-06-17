from roadtailbench_zoo.protocol import BaseAdapter, RTBControl


class ExternalModelStubAdapter(BaseAdapter):
    name = "external_stub"

    def setup(self, config):
        super().setup(config)
        self.model_name = self.config.get("model_name", "external_model")

    def run_step(self, observation):
        return RTBControl(
            brake=1.0,
            diagnostics={
                "model_name": self.model_name,
                "reason": "adapter_stub",
                "message": "Install the upstream model and implement model-specific preprocessing/postprocessing.",
            },
        )
