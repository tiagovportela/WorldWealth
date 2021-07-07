import numpy as np
import uuid
import random
import csv

import helpers

from settings import *


class Person:
    def __init__(self) -> None:
        self.id = str(uuid.uuid4())
        self.age = 0
        self.money = 0
        self.children = []
        self.dead_age = random.randint(60, 100)
        self.days_without_eat = 0

        self.alive = True

        self.genes = {
            'study': np.random.choice(a=[True, False], p=PROBABILITY_STUDY),
            'Spend Money': random.choice(SPEND_MONEY_PERCENTAGE),
            'baby': np.random.choice(a=[True, False], p=PROBABILITY_HAVE_CHILDREN),
            'Die Accident':  np.random.choice(a=[True, False], p=PROBABILITY_DIE_ACCIDENT),
            'Invest': np.random.choice(a=[True, False], p=PROBABILITY_INVEST)
        }
        self.invest_percentage = np.random.uniform(0.05, 0.2, size=1)[0]
        self.years_to_give_birth = helpers.bird_age()
        self.year_accident = int(np.random.normal(loc=30, scale=25, size=1))

    def have_money(self, value):
        if self.money > value:
            return True
        else:
            return False

    def work(self):
        if self.genes['study']:
            if self.age > WORKING_AGE and self.age < RETIREMENT_AGE:
                self.money += STUDY_COMPENSATION_GAIN*SALARY
        else:
            if self.age > LEGAL_AGE and self.age < RETIREMENT_AGE:
                self.money += SALARY

    def basic_needs(self):
        if self.have_money(BASIC_NEEDS):
            self.money -= BASIC_NEEDS
            self.days_without_eat = 0
        else:
            self.days_without_eat += 1

    def other_needs(self):
        spend_value = self.genes['Spend Money']*self.money
        if self.have_money(spend_value):
            if self.genes['study']:
                if self.age > WORKING_AGE:
                    self.money -= spend_value
            else:
                if self.age > LEGAL_AGE:
                    self.money -= spend_value

    def feed_children(self):
        for child in self.children:
            if child.age < LEGAL_AGE:
                if self.have_money(FEED_CHILD):
                    child.money += FEED_CHILD
                    self.money -= FEED_CHILD
            if self.genes['study'] and child.age < WORKING_AGE:
                if self.have_money(FEED_CHILD):
                    child.money += FEED_CHILD
                    self.money -= FEED_CHILD

    def invest(self):
        if self.genes['Invest']:
            if self.age > LEGAL_AGE:
                if self.genes['study']:
                    if self.age >= WORKING_AGE:
                        self.money += INTEREST_RATE*self.invest_percentage*self.money
                else:
                    self.money += INTEREST_RATE*self.invest_percentage*self.money

    def make_baby(self, population):
        if self.genes['baby']:
            if self.age in self.years_to_give_birth:
                baby = Person()
                self.children.append(baby)
                population.append(baby)

    def dead(self):
        try:
            heritage_value = self.money / len(self.children)
        except ZeroDivisionError:
            heritage_value = 0

        if self.age == self.dead_age:
            self.alive = False
            for child in self.children:
                child.money += heritage_value

        if self.days_without_eat > DAYS_DIE_WITHOUT_EATING:
            self.alive = False
            for child in self.children:
                child.money += heritage_value

        if self.genes['Die Accident']:
            if self.age == self.year_accident:
                self.alive = False

    def save(self):
        pass
