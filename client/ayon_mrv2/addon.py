import os
from ayon_core.addon import AYONAddon, IPluginPaths

from .version import __version__
from .constants import ADDON_NAME, MRV2_ROOT


class MRV2Addon(AYONAddon, IPluginPaths):
    """Addon adds mrv2 functionality via plugins."""

    name = ADDON_NAME
    version = __version__

    def get_plugin_paths(self):
        return {
            "load": self.get_load_plugin_paths()
        }

    def get_load_plugin_paths(self, host_name=None):
        return [
            os.path.join(MRV2_ROOT, "plugins", "load"),
        ]

    def get_ftrack_event_handler_paths(self):
        return {
            "user": [
                os.path.join(MRV2_ROOT, "plugins", "ftrack"),
            ]
        }
