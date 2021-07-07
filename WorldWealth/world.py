import csv
import datetime
from influxdb import InfluxDBClient

from agent import Person


class World:
    def __init__(self, initial_population, name) -> None:

        self.name = name
        self.population = []
        self.initial_population = initial_population
        self.dead_population = []

    def create_world(self):

        self.client = InfluxDBClient(host='localhost', port=8086)

        self.client.drop_database(self.name)

        self.client.create_database(self.name)
        self.client.switch_database(self.name)

        for i in range(self.initial_population):
            person = Person()
            person.age = 35
            self.population.append(person)

    # def save_data(self, person, day):
    #     with open('population.csv', mode='a') as population_file:
    #         population_writer = csv.writer(
    #             population_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    #         population_writer.writerow(
    #             [person.id, person.age, person.money, len(person.children), day])

    def save_data(self, person, year):
        date_time = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S.%f")

        data = {
            'id': person.id,
            'age': person.age,
            'children': len(person.children),
            'money': float(person.money),
            'days_without_eat': person.days_without_eat,
            'Year': year
        }

        json_body = [
            {
                "measurement": self.name,
                "time": date_time,
                "fields": data
            }

        ]

        self.client.write_points(json_body)

    def run(self, Year):

        if Year % 50 == 0:
            print(f'Year: {Year}')
            print(f'Population: {len(self.population)}')
            print('-'*35)

        for person in self.population:
            person.work()
            person.basic_needs()
            person.feed_children()
            person.other_needs()
            person.make_baby(self.population)
            person.invest()
            person.dead()
            person.age += 1

            if not person.alive:
                self.population.remove(person)
                self.dead_population.append(person)
            self.save_data(person, Year)
