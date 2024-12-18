import os
import time

import clique

from ayon_core.lib import run_detached_process
from ayon_core.lib.transcoding import IMAGE_EXTENSIONS, VIDEO_EXTENSIONS
from ayon_core.pipeline import load

from ayon_mrv2.utils import MRV2ExecutableCache


class OpenInMRV2(load.LoaderPlugin):
    """Open Image Sequence with system default"""

    _executable_cache = MRV2ExecutableCache()
    product_types = ["*"]
    representations = ["*"]
    extensions = {
        ext.lstrip(".")
        for ext in set(IMAGE_EXTENSIONS) | set(VIDEO_EXTENSIONS)
    }

    label = "Open in MRV2"
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

        path = self.filepath_from_context(context)
        directory = os.path.dirname(path)

        pattern = clique.PATTERNS["frames"]
        files = os.listdir(directory)
        collections, remainder = clique.assemble(
            files,
            patterns=[pattern],
            minimum_items=1
        )

        if not remainder:
            sequence = collections[0]
            first_image = list(sequence)[0]
        else:
            first_image = path
        filepath = os.path.normpath(os.path.join(directory, first_image))

        self.log.info("Opening : {}".format(filepath))

        executable = self.get_mrv2_path()
        cmd = [
            # MRV2 path
            str(executable),
            # PATH TO COMPONENT
            filepath
        ]

        try:
            # Run MRV2 with these commands
            run_detached_process(cmd)
            # Keep process in memory for some time
            time.sleep(0.1)

        except FileNotFoundError:
            self.log.error(
                f"File \"{os.path.basename(filepath)}\" was not found."
            )
