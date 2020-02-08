"""ForeCut Pipeline :: Generate predictions"""


from forecut_pipeline import Pipeline


class Predict(Pipeline):
    """Pipeline task for performing predictions."""

    def __init__(self, model):
        self.model = model

        super().__init__()

    def map(self, data):
        image = data["image"]
        results = self.model.detect([image], verbose=1)
        data["predictions"] = predictions

        return data

