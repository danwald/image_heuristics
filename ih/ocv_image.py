from image import ImageInterface
from ops import QualityOpsInterface

import cv

class OpenCVImage(ImageInterface, QualityOpsInterface):
    def __init__(self, filename):
        self.filename = filename
        self.image = None

    def load_image(self):
        self.image = cv2.imread(self.filename, cv2.IMREAD_ANYCOLOR)
 
    def save_image(self, filename=''):
        self.image.imwrite(filename if filename and len(filename) else self.filename)

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
