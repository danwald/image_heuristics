from abc import ABCMeta, abstractmethod


class ImageInterface(object):
    @abstractmethod
    def load_image():
        pass
 
    @abstractmethod
    def save_image(filename):
        pass
