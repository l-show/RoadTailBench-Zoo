from .external_stub import ExternalModelStubAdapter


class AlpamayoAdapter(ExternalModelStubAdapter):
    name = "alpamayo"

    def setup(self, config):
        super().setup({**(config or {}), "model_name": "Alpamayo"})
