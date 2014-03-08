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
       self.gray_image = None
       self.original_color_image = None

    def load_image(self):
        self.image = cv2.imread(self.filename, cv.CV_LOAD_IMAGE_UNCHANGED)
        if self.image == None:
            raise(AttributeError("Failed to load image from '%s'"%(self.filename)))
 
    def save_image(self, filename=''):
        cv2.imwrite(filename if filename and len(filename) else self.filename, self.image)

    def is_color(self):
        if self.original_color_image == None:
            try:
                if self.image.shape[2] == 3:
                    #checking first 2 channels to see if this is a 3 channel gray
                    #get second channel
                    _1 = self.image[...,1]
                    #make it a list
                    _1 = _1.reshape( _1.shape[0]*_1.shape[1])
                    #rinse
                    _0 = self.image[...,0]
                    #repeat
                    _0 = _0.reshape(_0.shape[0]*_0.shape[1])
                    self.original_color_image = False
                    #TODO: begging for a list comprehension
                    for i, j in zip(_0, _1):
                        if i != j:
                            self.original_color_image = True
                            break
                    if self.original_color_image:
                        self.gray_image = cv2.cvtColor(self.image, cv.CV_BGR2GRAY)
                    else:
                        #just take the first channel
                        self.image = self.image[...,0].copy()
            except IndexError:
                self.gray_image = self.image
                self.original_color_image = False
        return self.original_color_image

    def is_over_under_exposed(self):
        pass

    def is_blurry(self):
        pass

    def is_noisy(self):
        pass

    def get_signature(self):
        return hashlib.sha1(self.image.data).hexdigest()
