from typing import Type

from ayon_server.addons import BaseServerAddon

from .settings import Mrv2settings, DEFAULT_VALUES


class Mrv2Addon(BaseServerAddon):
    settings_model: Type[Mrv2settings] = Mrv2settings

    async def get_default_settings(self):
        settings_model_cls = self.get_settings_model()
        return settings_model_cls(**DEFAULT_VALUES)
