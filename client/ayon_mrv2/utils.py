import os
import time
import platform

import ayon_api

from .version import __version__
from .constants import ADDON_NAME


def get_mrv2_icon_url(server_url=None):
    """Get URL to MRV2 icon.

    Args:
        server_url (Optional[str]): AYON server URL.

    Returns:
        str: URL where MRV2 icon is located.
    """

    server_url = server_url or ayon_api.get_base_url()
    return "{}/addons/{}/{}/public/mrv2.png".format(
        server_url, ADDON_NAME, __version__
    )


def get_mrv2_paths_from_settings(addon_settings=None):
    """

    Args:
        addon_settings (Optional[dict[str, Any]): Addon settings.

    Returns:
        list[str]: List to MRV2 executable paths. Paths are not validated.
    """

    if addon_settings is None:
        addon_settings = ayon_api.get_addon_settings(ADDON_NAME, __version__)

    platform_name = platform.system().lower()
    return addon_settings.get("mrv2_path", {}).get(platform_name, [])


def get_mrv2_executable_path(paths=None, addon_settings=None):
    """

    Args:
        paths (Optional[list[str]]): List of paths to MRV2 executable.
        addon_settings (Optional[dict[str, Any]): Addon settings.

    Returns:
        list[str]: List of available paths to MRV2 executable.
    """

    if paths is None:
        paths = get_mrv2_paths_from_settings(addon_settings)

    for path in paths:
        if path and os.path.exists(path):
            return path
    return None


class MRV2ExecutableCache:
    lifetime = 10

    def __init__(self):
        self._cached_time = None
        self._mrv2_paths = None
        self._mrv2_path = None

    def is_cache_valid(self):
        """Cache is valid.

        Returns:
            bool: True if cache is valid, False otherwise.
        """

        if self._cached_time is None:
            return False

        start = time.time()
        return (start - self._cached_time) <= self.lifetime

    def get_paths(self):
        """Get all paths to MRV2 executable from settings.

        Returns:
            list[str]: Path to MRV2 executables.
        """

        if not self.is_cache_valid():
            self._mrv2_paths = get_mrv2_paths_from_settings()
            self._cached_time = time.time()
        return self._mrv2_paths

    def get_path(self):
        """Get path to MRV2 executable.

        Returns:
            Union[str, None]: Path to MRV2 executable or None.
        """

        if not self.is_cache_valid():
            self._mrv2_path = get_mrv2_executable_path(self.get_paths())
        return self._mrv2_path
