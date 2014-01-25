from abc import ABCMeta, abstractmethod


class QualityOpsInterface:
    @abstractmethod
    def is_color():
        pass

    @abstractmethod
    def is_over_under_exposed():
        pass

    @abstractmethod
    def is_blurry():
        pass

    @abstractmethod
    def is_noisy():
        pass

    @abstractmethod
    def get_signature():
        pass
