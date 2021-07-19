import numpy as np

from .constants import *
from .parameters import *
#from .helpers import save_person_data


class Company:
    def __init__(self, world) -> None:

        self.world = world

        self.employees = []
        self.money = 1_000_000
        self.goods = 0

    def produce_goods(self) -> None:

        produced_goods = NUMBER_PRODUTS_MADE_BY_EMPLOYEE*len(self.employees)
        if self.world.resources.extract(produced_goods):
            self.goods += produced_goods

    def sell_goods(self, value) -> None:
        if self.goods > 0:
            self.money += value
            self.goods -= 1
            return True
        else:
            return False

    def pay_wage(self, value) -> bool:
        if self.money > value:
            self.money -= value
            return True
        else:
            return False

    def pay_taxes(self, state):
        amount = self.money*IRC_TAX

        state.money += amount
        self.money -= amount

    def hire(self, person) -> None:
        person.hired = True
        self.employees.append(person)
