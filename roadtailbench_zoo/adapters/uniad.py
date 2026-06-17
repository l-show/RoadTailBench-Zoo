from .external_stub import ExternalModelStubAdapter


class UniADAdapter(ExternalModelStubAdapter):
    name = "uniad"

    def setup(self, config):
        super().setup({**(config or {}), "model_name": "UniAD"})
