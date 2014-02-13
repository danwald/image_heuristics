import cv2

from image import ImageInterface
from ops import QualityOpsInterface


class OpenCVImage(ImageInterface, QualityOpsInterface):
    def _loaded(func):
        def inner(self, *args, **kwargs):
            if not self.image:
                self.load_image()
            func(self, *args, **kwargs)
        return inner

    def __init__(self, filename):
        self.filename = filename
        self.image = None

    def load_image(self):
        self.image = cv2.imread(self.filename, cv2.IMREAD_ANYCOLOR)
 
    @_loaded
    def save_image(self, filename=''):
        cv2.imwrite(filename if filename and len(filename) else self.filename, self.image)

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
