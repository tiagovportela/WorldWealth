import numpy as np
import uuid

from .constants import *
from .parameters import *
from .helpers import *


class Person:
    """
    A class to represent a person.

    ...

    Attributes
    ----------
    state: object
        state that a person belongs to. 
    id : str
        id of the person
    age : int
        age of the person
    money : float
        money of the person
    death_age : int
        age that a person will die
    children : list
        children that a person have
    alive : bool
        atribute that indicates if a person is alive
    working : bool
        atribute that indicates if a person is working
    days_without_basic_needs : int
        how many years a person is alive without providing basic needs 
    working_sector : str
        setor for that person work
    DNA : dict
        Dict with genetic information
    percentage_money_invest : float
        percentage of money that a person will invest 
    age_premature_death : int
        age that a person will die prematurely
    children_birth_age : list
        ages that a person will give to birth
    cause_of_death : str
        cause of person dead
    hired : bool
        atribute that indicates if a person is hired by company

    Methods
    -------

    """

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
        self.working_sector = None

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
        self.cause_of_death = None

        self.hired = False

    # check if have the amount to spend

    def have_money(self, amount) -> bool:
        if self.money > amount:
            return True
        else:
            False

    def work(self, company) -> None:
        if self.working:
            if self.DNA[STUDY]:
                wage = STUDY_COMPENSATION_GAIN*YEAR_INCOME
                if company.pay_wage(wage):
                    self.money += wage

            else:
                if company.pay_wage(YEAR_INCOME):
                    self.money += YEAR_INCOME

    def meet_basic_needs(self, company) -> None:
        if self.age >= LEGAL_AGE:
            if self.have_money(BASIC_NEEDS_ADULT):
                if company.sell_goods(BASIC_NEEDS_ADULT):
                    self.money -= BASIC_NEEDS_ADULT
                    self.days_without_basic_needs = 0
                else:
                    self.days_without_basic_needs += 1
            else:
                self.days_without_basic_needs += 1
        else:
            if self.have_money(BASIC_NEEDS_CHILD):
                if company.sell_goods(BASIC_NEEDS_CHILD):
                    self.money -= BASIC_NEEDS_CHILD
                    self.days_without_basic_needs = 0
                else:
                    self.days_without_basic_needs += 1
            else:
                self.days_without_basic_needs += 1

    def other_needs(self, company) -> None:
        amount = self.DNA[S_MONEY] * \
            amount_to_spend_on_other_needs(self.money, len(self.children))
        amount += VAT_TAX*amount

        self.state.money += VAT_TAX*amount

        if self.working and self.have_money(amount):
            self.money -= amount
            company.sell_goods(amount)

    def feed_children(self) -> None:
        for child in self.children:
            if not child.working:
                if self.have_money(FEED_CHILD):
                    child.money += FEED_CHILD
                    self.money -= FEED_CHILD

    def invest(self) -> None:
        if self.DNA[INVEST]:
            if self.working:
                self.money += INTEREST_RATE*self.percentage_money_invest \
                    * self.money

    def make_baby(self, population) -> None:
        if self.DNA[BABY]:
            if self.age in self.children_birth_age:
                baby = Person(self.state)
                self.children.append(baby)
                population.append(baby)

    # kill a person and distibute his wealth for crildren
    #  or give than to state.
    def die(self) -> None:

        if len(self.children) > 0:
            heritage_value = self.money / len(self.children)
        else:
            heritage_value = 0

        if self.state.allow_heritage:
            for child in self.children:
                child.money += heritage_value
        else:
            self.state.money += STATE_EFFIENCY * heritage_value

        self.alive = False

    def death_state(self) -> None:

        if self.age == self.death_age:
            self.die()
            self.cause_of_death = NATURAL

        if self.DNA[P_DEATH]:
            if self.age == self.age_premature_death:
                self.die()
                self.cause_of_death = PREMATURE
        if self.days_without_basic_needs >= MAX_DAYS_WITHOUT_BASIC_NEEDS:
            self.die()
            self.cause_of_death = CANT_PROVED_BASIC_NEEDS

    def working_state(self) -> None:
        if self.age <= RETIREMENT_AGE:
            if self.DNA[STUDY]:
                if self.age >= WORKING_AGE:
                    self.working = True
                    self.working_sector = choose_work_sector()
            else:
                if self.age >= LEGAL_AGE:
                    self.working = True
                    self.working_sector = choose_work_sector()
        else:
            self.working = False
