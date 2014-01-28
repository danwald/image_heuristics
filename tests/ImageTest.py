import unittest
import os

from ih.ocv_image import OpenCVImage

class IntstantiationTest(unittest.TestCase):
    def setUp(self):
        pass

    def CreateOpenCVImageTest(self):
        image =  OpenCVImage("dummy")
