import multiprocessing as mp
from worldwealth import Person

pool = mp.Pool(mp.cpu_count())

population = []
dead_population = []
age_dead = []

for i in range(20):
    person = Person()
    person.age = 35
    population.append(person)

def process_person_life_year(person):
    person.working_state()
    person.work()
    person.meet_basic_needs()
    person.feed_children()
    person.invest()
    person.other_needs()
    person.make_baby(population)

    person.death_state()
    person.age += 1

    if not person.alive:
        age_dead.append(person.age)
        population.remove(person)
        dead_population.append(person)
    with open('population.csv', mode='a') as population_file:
        population_writer = csv.writer(
            population_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        population_writer.writerow(
            [person.id, person.age, person.money, len(person.children), Year])    

try:
    os.remove('population.csv') 
except:
    print('OK')
for Year in range(1000):
        #if Year % 50 == 0:
            #print(f'Year: {Year}')
            #print(f'Population: {len(population)}')
            #print('-'*35)
        pool.map(process_person_life_year,population) 
        pool.close()