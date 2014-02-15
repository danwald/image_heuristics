import unittest

from ih.ocv_image import OpenCVImage

class IntstantiationTest(unittest.TestCase):
    def setUp(self):
        self.OUTPUT_FILENAME = "/tmp/test.jpg"
        self.image = OpenCVImage("images/lena.jpg")
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
        grey_image = OpenCVImage("images/lena_grey.jpg")
        grey_image.load_image()
        self.assertTrue(not grey_image.is_color())

    def test_color_image(self):
        self.assertTrue(self.image.is_color())
