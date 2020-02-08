"""rmbg Pipeline :: load single image file"""

import skimage.io

from forecut_pipeline.pipeline import Pipeline


class CaptureImage(Pipeline):
    """Pipeline task to capture single image file."""

    def __init__(self, src):
        self.src = src

        super().__init__()

    def generator(self):
        """Yields the image content and metadata."""

        image = skimage.io.imread(self.src)

        data = {"image_id": self.src, "image": image}

        if self.filter(data):
            yield self.map(data)
