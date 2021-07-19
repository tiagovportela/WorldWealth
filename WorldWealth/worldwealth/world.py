import numpy as np
import csv
import pandas as pd

from .parameters import *

from .person import Person
from .state import State
from .resources import Resources
from .companies import Company

from .helpers import save_person_data
from .helpers import save_state_data
from .helpers import save_company_data


class World:
    def __init__(self,
                 name,
                 initial_population,
                 years_until_extintion,
                 allow_heritage,
                 wealth_distribution,
                 initial_resources,
                 number_companies

                 ) -> None:
        self.name = name
        self.initial_population = initial_population
        self.years_until_extintion = years_until_extintion

        #self.allow_heritage = allow_heritage
        #self.wealth_distribution = wealth_distribution

        self.current_year = 0

        self.population = []
        self.dead_population = []

        self.state = State(
            allow_heritage=allow_heritage,
            wealth_distribution=wealth_distribution
        )

        self.resources = Resources(
            initial_resources=initial_resources
        )

        self.companies = [Company(self) for _ in range(number_companies)]

    def create_world(self):
        for _ in range(self.initial_population):
            person = Person(self.state)
            person.age = 35
            self.population.append(person)

    # def genarete_resources(self):
    #     if self.current_year % YEARS_TO_REGENERATE_RESOURCES == 0:
    #         self.resources += len(self.population)*5*YEAR_INCOME

    def process_person_life(self, person):
        # print('Processing!')
        person.working_state()
        person.work(self.companies[0])
        person.meet_basic_needs(self.companies[0])
        person.feed_children()
        person.invest()
        person.other_needs(self.companies[0])
        person.make_baby(self.population)

        person.death_state()
        person.age += 1

        if not person.alive:

            self.population.remove(person)
            self.dead_population.append(person)

        save_person_data(person, self.current_year)

    def run(self):
        # self.create_world()
        self.current_year = 0
        while (self.current_year < self.years_until_extintion):

            self.state.population = self.population
            #pool_obj = multiprocessing.Pool()
            #pool_obj.map(self.process_person_life_year, self.population)

            # if self.current_year % 50 == 0:
            self.resources.genarete()

            for company in self.companies:
                company.produce_goods()

            save_state_data(self.state, self.current_year)

            for person in self.population:
                # works only one companie
                if person.working and not person.hired:
                    self.companies[0].hire(person)

                self.state.distribute_wealth(person)
                self.process_person_life(person)
                self.state.collect_taxes(person)

            self.companies[0].pay_taxes(self.state)

            save_company_data(self.companies[0], self.current_year)

            self.current_year += 1
