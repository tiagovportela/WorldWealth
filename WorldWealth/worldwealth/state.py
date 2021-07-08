import numpy as np

from .constants import *
from .parameters import *
from .helpers import *


class State:
    def __init__(self, allow_heritage, wealth_distribution) -> None:

        self.allow_heritage = allow_heritage
        self.wealth_distribution = wealth_distribution
        self.population = []

        self.money = 0

    def collect_taxes(self, person):

        if self.wealth_distribution:
            if person.working:
                person.money -= person.money*BASE_TAX
                self.money += person.money*BASE_TAX

    def distribute_wealth(self, person):

        value_to_distribute = self.money / len(self.population)

        if self.wealth_distribution:
            if person.working:
                person.money += value_to_distribute
                self.money -= value_to_distribute
