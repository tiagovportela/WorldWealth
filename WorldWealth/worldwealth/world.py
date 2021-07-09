import numpy as np
import csv
import pandas as pd

from .person import Person
from .state import State
from .helpers import save_person_data


class World:
    def __init__(self,
                 name,
                 initial_population,
                 years_until_extintion,
                 allow_heritage,
                 wealth_distribution

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

    def create_world(self):
        for _ in range(self.initial_population):
            person = Person(self.state)
            person.age = 35
            self.population.append(person)

    def process_person_life(self, person):
        # print('Processing!')
        person.working_state()
        person.work()
        person.meet_basic_needs()
        person.feed_children()
        person.invest()
        person.other_needs()
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
            with open('./state.csv', mode='a') as state_file:
                state_writer = csv.writer(
                    state_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

                state_writer.writerow(
                    [self.state.money, self.current_year])

            for person in self.population:
                self.state.distribute_wealth(person)
                self.process_person_life(person)
                self.state.collect_taxes(person)

            self.current_year += 1
