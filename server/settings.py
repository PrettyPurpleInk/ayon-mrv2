from ayon_server.settings import (
    BaseSettingsModel,
    SettingsField,
    MultiplatformPathListModel,
)


class MRV2Settings(BaseSettingsModel):
    """MRV2 addon settings."""

    enabled: bool = SettingsField(True)
    mrv2_path: MultiplatformPathListModel = SettingsField(
        title="MRV2 paths",
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
        "linux": [],
        "darwin": [
            "/Applications/MRV2.app/Contents/MacOS/MRV2",
        ]
    }
}
