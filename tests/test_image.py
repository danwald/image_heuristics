import unittest

from ih.ocv_image import OpenCVImage


class IntstantiationTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_load_image(self):
        image = OpenCVImage("dummy")

    def test_save_image(self):
        image = OpenCVImage("dummy")
        image.save_image()
