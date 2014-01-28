from image import ImageInterface
from ops import QualityOpsInterface

class OpenCVImage(ImageInterface, QualityOpsInterface):
    def __init__(self, filename):
        self.filename = filename

    def load_image(self):
        pass
 
    def save_image(self):
        pass

    def is_color(self):
        pass

    def is_over_under_exposed(self):
        pass

    def is_blurry(self):
        pass

    def is_noisy(self):
        pass

    def get_signature(self):
        pass
