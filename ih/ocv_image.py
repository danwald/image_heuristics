import inspect
import hashlib

import cv
import cv2

from image import ImageInterface
from ops import QualityOpsInterface


class OpenCVImage(ImageInterface, QualityOpsInterface):
    def __init__(self, filename):
       self.filename = filename
       self.image = None

    def load_image(self):
        self.image = cv2.imread(self.filename, cv.CV_LOAD_IMAGE_UNCHANGED)
        if self.image == None:
            raise(AttributeError("Failed to load image from '%s'"%(self.filename)))
 
    def save_image(self, filename=''):
        cv2.imwrite(filename if filename and len(filename) else self.filename, self.image)

    def is_color(self):
        try:
            return self.image.shape[2] == 3
        except IndexError:
            return False

    def is_over_under_exposed(self):
        pass

    def is_blurry(self):
        pass

    def is_noisy(self):
        pass

    def get_signature(self):
        return hashlib.sha1(self.image.data).hexdigest()
