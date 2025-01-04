from ayon_server.settings import (
    BaseSettingsModel,
    SettingsField,
    MultiplatformPathListModel,
)


class Mrv2settings(BaseSettingsModel):
    """mrv2 addon settings."""

    enabled: bool = SettingsField(True)
    mrv2_path: MultiplatformPathListModel = SettingsField(
        title="mrv2 paths",
        default_factory=MultiplatformPathListModel,
        scope=["studio"],
    )

# TODO: Paths
DEFAULT_VALUES = {
    "enabled": True,
    "mrv2_path": {
        "windows": [
            "C:\\Program Files\\mrv2-v1.3.0\\bin\\mrv2.exe",
        ],
        "linux": [
            "/usr/bin/mrv2",
            "/usr/local/mrv2-v1.3.0-Linux-64/bin/mrv2.sh",
        ],
        "darwin": [
            "/Applications/mrv2.app/Contents/MacOS/mrv2",
        ]
    }
}
