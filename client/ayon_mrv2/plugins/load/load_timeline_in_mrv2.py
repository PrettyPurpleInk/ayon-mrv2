import os
import time

from ayon_core.lib import run_detached_process
from ayon_core.pipeline import load
#from ayon_core.pipeline import editorial

from ayon_mrv2.utils import Mrv2ExecutableCache


class LoadTimelineInMrv2(load.LoaderPlugin):
    """Open Image Sequence with system default"""

    _executable_cache = Mrv2ExecutableCache()
    product_types = ["*"]
    representations = ["*"]
    extensions = { "otio" }

    label = "Load in mrv2"
    order = -10
    icon = "play-circle"
    color = "orange"

    @classmethod
    def get_mrv2_path(cls):
        return cls._executable_cache.get_path()

    @classmethod
    def is_compatible_loader(cls, context):
        if not cls.get_mrv2_path():
            return False
        return super().is_compatible_loader(context)

    def load(self, context, name, namespace, data):
        filepath = os.path.normpath(self.filepath_from_context(context))
        self.log.info(f"Opening : {filepath}")

        executable = self.get_mrv2_path()
        cmd = [
            # mrv2 path
            str(executable),
            # PATH TO COMPONENT
            filepath
        ]

        try:
            # Run mrv2 with these commands
            run_detached_process(cmd)
            # Keep process in memory for some time
            time.sleep(0.1)

        except FileNotFoundError:
            self.log.error(
                f"File \"{os.path.basename(filepath)}\" was not found."
            )
