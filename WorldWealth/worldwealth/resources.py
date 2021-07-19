from .parameters import *


class Resources:
    def __init__(self, initial_resources) -> None:

        self.available_resources = initial_resources

    def extract(self, value):
        if self.available_resources > value:
            self.available_resources -= value
            return True
        else:
            return False

    def genarete(self):
        self.available_resources += BASE_RESOURCES
