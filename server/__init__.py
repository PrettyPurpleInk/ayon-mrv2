from typing import Type

from ayon_server.addons import BaseServerAddon

from .settings import MRV2Settings, DEFAULT_VALUES


class MRV2Addon(BaseServerAddon):
    settings_model: Type[MRV2Settings] = MRV2Settings

    async def get_default_settings(self):
        settings_model_cls = self.get_settings_model()
        return settings_model_cls(**DEFAULT_VALUES)
