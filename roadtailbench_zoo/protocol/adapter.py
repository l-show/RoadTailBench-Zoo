from .types import RTBControl


class BaseAdapter:
    name = "base"

    def setup(self, config):
        self.config = config or {}

    def sensors(self):
        return []

    def run_step(self, observation):
        return RTBControl()

    def destroy(self):
        pass
