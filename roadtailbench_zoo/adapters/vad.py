from .external_stub import ExternalModelStubAdapter


class VADAdapter(ExternalModelStubAdapter):
    name = "vad"

    def setup(self, config):
        super().setup({**(config or {}), "model_name": "VAD"})
