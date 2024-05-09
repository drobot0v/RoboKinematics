from abc import ABC, abstractmethod


class ET(ABC):

    @abstractmethod
    def perform(self, *args, **kwargs):
        pass


class Rot2(ET):

    def perform(self, *args, **kwargs):
        return super().perform(*args, **kwargs)