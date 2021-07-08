import numpy as np
import uuid

from .constants import *
from .parameters import *
from .helpers import *


class Person:
    def __init__(self, state) -> None:

        self.state = state

        self.id = str(uuid.uuid4())
        self.age = 0
        self.money = 0
        self.death_age = death_age()
        self.children = []

        self.alive = True
        self.working = False
        self.days_without_basic_needs = 0

        self.DNA = {
            STUDY: gene(STUDY),
            BABY: gene(BABY),
            P_DEATH: gene(P_DEATH),
            INVEST: gene(INVEST),
            S_MONEY: gene(S_MONEY)
        }

        self.percentage_money_invest = percentage_money_person_will_invest()
        self.children_birth_age = children_birth_age()
        self.age_premature_death = age_premature_death()

    # check if have the amount to spend
    def have_money(self, amount) -> bool:
        if self.money > amount:
            return True
        else:
            False

    def work(self) -> None:
        if self.working:
            if self.DNA[STUDY]:
                self.money += STUDY_COMPENSATION_GAIN*SALARY
            else:
                self.money += SALARY

    def meet_basic_needs(self) -> None:
        if self.age >= LEGAL_AGE:
            if self.have_money(BASIC_NEEDS_ADULT):
                self.money -= BASIC_NEEDS_ADULT
                self.days_without_basic_needs = 0
            else:
                self.days_without_basic_needs += 1
        else:
            if self.have_money(BASIC_NEEDS_CHILD):
                self.money -= BASIC_NEEDS_CHILD
                self.days_without_basic_needs = 0
            else:
                self.days_without_basic_needs += 1

    def other_needs(self) -> None:
        amount = self.DNA[S_MONEY]*SALARY
        if self.working and self.have_money(amount):
            self.money -= amount

    def feed_children(self) -> None:
        for child in self.children:
            if not child.working:
                if self.have_money(FEED_CHILD):
                    child.money += FEED_CHILD
                    self.money -= FEED_CHILD

    def invest(self) -> None:
        if self.DNA[INVEST]:
            if self.working:
                self.money += INTEREST_RATE*self.percentage_money_invest*self.money

    def make_baby(self, population) -> None:
        if self.DNA[BABY]:
            if self.age in self.children_birth_age:
                baby = Person(self.state)
                self.children.append(baby)
                population.append(baby)

    # kill a person and distibute his wealth for crildren.
    def die(self) -> None:
        try:
            heritage_value = self.money / len(self.children)
        except:
            heritage_value = 0

        if self.state.allow_heritage:
            for child in self.children:
                child.money += heritage_value
        else:
            self.state.money += heritage_value

        self.alive = False

    def death_state(self) -> None:

        if self.age == self.death_age:
            self.die()

        if self.DNA[P_DEATH]:
            if self.age == self.age_premature_death:
                self.die()
        if self.days_without_basic_needs >= MAX_DAYS_WITHOUT_BASIC_NEEDS:
            self.die()

    def working_state(self) -> None:
        if self.age <= RETIREMENT_AGE:
            if self.DNA[STUDY]:
                if self.age >= WORKING_AGE:
                    self.working = True
            else:
                if self.age >= LEGAL_AGE:
                    self.working = True
        else:
            self.working = False
