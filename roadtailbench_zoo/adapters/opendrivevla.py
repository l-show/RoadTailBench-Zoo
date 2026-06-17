from .external_stub import ExternalModelStubAdapter


class OpenDriveVLAAdapter(ExternalModelStubAdapter):
    name = "opendrivevla"

    def setup(self, config):
        super().setup({**(config or {}), "model_name": "OpenDriveVLA"})
