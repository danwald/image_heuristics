import unittest
from nose.tools import *

from ih.ocv_image import OpenCVImage

class IntstantiationTest(unittest.TestCase):
    def setUp(self):
        self.COLOR_IMAGE_FILENAME = "images/lena.jpg"
        self.GREY_IMAGE_FILENAME = "images/lena_grey.jpg"
        self.OUTPUT_FILENAME = "/tmp/test.jpg"
        self.image = OpenCVImage(self.COLOR_IMAGE_FILENAME)
        self.image.load_image()

    def test_load_image(self):
        self.image.load_image()

    def test_save_image_with_old_filename(self):
        self.image.save_image(self.OUTPUT_FILENAME)
        image2 = OpenCVImage(self.OUTPUT_FILENAME)
        image2.load_image()
        image2.save_image()

    def test_save_image_with_new_filename(self):
        self.image.save_image(self.OUTPUT_FILENAME)

    def test_grey_image(self):
        grey_image = OpenCVImage(self.GREY_IMAGE_FILENAME)
        grey_image.load_image()
        self.assertTrue(not grey_image.is_color())

    def test_color_image(self):
        self.assertTrue(self.image.is_color())

    def test_signature(self):
        image2 = OpenCVImage(self.COLOR_IMAGE_FILENAME)
        image2.load_image()
        self.assertTrue(self.image.get_signature() == image2.get_signature())
    
    @raises(AttributeError)
    def test_bad_filename(self):
        image2 = OpenCVImage("bad_image.jpg")
        image2.load_image()

    def test_another_grey_image(self):
        grey_image = OpenCVImage("images/image_test_bw.jpg")
        grey_image.load_image()
        self.assertTrue(not grey_image.is_color())
