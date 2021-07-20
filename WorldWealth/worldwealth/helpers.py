import numpy as np
import random
import csv

from .constants import *
from .parameters import *

np.random.seed(1)


def gene(type):
    '''
    Return the values for the genes

        Parameters:
            (string) type: type of gene

        Returns
            (bool) Returns a bool indicating if gene is active

    '''
    if type == STUDY:
        return random.choices([True, False],
                              weights=PROBABILITY_STUDY,
                              k=1
                              )[0]

    elif type == BABY:
        return random.choices([True, False],
                              weights=PROBABILITY_HAVE_CHILDREN,
                              k=1
                              )[0]

    elif type == P_DEATH:
        return random.choices([True, False],
                              weights=PROBABILITY_P_DEATH,
                              k=1
                              )[0]
    elif type == INVEST:
        return random.choices([True, False], weights=PROBABILITY_INVEST,
                              k=1
                              )[0]
    elif type == S_MONEY:
        return np.random.choice(SPEND_MONEY_PERCENTAGE)


def percentage_money_person_will_invest():
    '''
    Return percentage of money that a person will invest.
    Sampled from a uniform distribution

        Parameters:
            None

        Returns
            (float) Returns a float with percentage of money that a person
            will invest

    '''
    return np.random.uniform(0.05, 0.2, size=1)[0]


def number_of_children_person_will_have():
    '''
    Return the number of children that a person will have.
    Sample from normal distribution.
    Used in children_birth_age()

        Parameters:
            None
        Retuns
            (int): number of children that a person will have
    '''
    return abs(int(np.random.normal(MEAN_CHILDREN, STD_CHILDREN)))


def children_birth_age():
    '''
    Return the ages at a person will give birth to the children.
    Sample from normal distribution.

        Parameters:
            None
        Retuns
            (list): list with ages that a person will give birth
    '''
    ages = []
    min_age, max_age = FERTILE_YEARS
    number_of_children = number_of_children_person_will_have()

    while(len(ages) < number_of_children):
        age = abs(
            int(
                np.random.normal(
                    MEAN_BIRTH_CHILD_AGE,
                    STD_BIRTH_CHILD_AGE
                )
            )
        )
        if age not in ages:
            if age > min_age and age < max_age:
                ages.append(age)
    return ages


def age_premature_death():
    '''
    Return the age of premature death.
    Sample from normal distribution.

        Parameters:
            None
        Retuns
            (int) age: age of premature death
    '''
    age = []
    min_age, max_age = P_DEATH_RANGE
    while(len(age) < 1):
        value = int(
            np.random.normal(loc=MEAN_P_DEATH, scale=STD_P_DEATH, size=1))
        if value > min_age and value < max_age:
            age.append(value)
    return age[0]

# Return age of death


def death_age():
    '''
    Return the age of death.
    Sample from normal distribution.

        Parameters:
            None
        Retuns
            (int) age: age of death
    '''
    age = []
    min_age, max_age = DEATH_RANGE
    while(len(age) < 1):
        value = int(
            np.random.normal(loc=MEAN_DEATH, scale=STD_DEATH, size=1))
        if value > min_age and value < max_age:
            age.append(value)
    return age[0]


def amount_to_spend_on_other_needs(money, number_children):
    '''
    Returns the money spent in other needs than the basics
    For that is calculate the base_amount that is used for calculate the rank
    of wealth (Disponibility for spend mone)

        Parameters:
            (float) money: money that a person have
            (int) number of children that a person have

        Return:
            (float): money spent
    '''

    first = WEALTH_RANKS['FIRST']
    second = WEALTH_RANKS['SECOND']
    third = WEALTH_RANKS['THIRD']
    fourth = WEALTH_RANKS['FOURTH']
    fifth = WEALTH_RANKS['FIFTH']

    base_amout = number_children*FEED_CHILD + BASIC_NEEDS_ADULT

    if money >= first[0]*base_amout and money < first[1]*base_amout:
        return YEAR_INCOME*first[2]
    elif money >= second[0]*base_amout and money < second[1]*base_amout:
        return YEAR_INCOME*second[2]
    elif money >= third[0]*base_amout and money < third[1]*base_amout:
        return YEAR_INCOME*third[2]
    elif money >= fourth[0]*base_amout and money < fourth[1]*base_amout:
        return YEAR_INCOME*fourth[2]
    elif money >= fifth[0]:
        return YEAR_INCOME*fifth[2]
    else:
        return YEAR_INCOME


def choose_work_sector():
    return np.random.choice(
        a=[PRIMARY, SECONDARY, TERTIARY],
        p=PROBABILITY_WORK_SECTOR
    )


def save_company_data(company, year):
    with open('./company.csv', mode='a') as state_file:
        state_writer = csv.writer(
            state_file,
            delimiter=',',
            quotechar='"',
            quoting=csv.QUOTE_MINIMAL
        )

        state_writer.writerow(
            [company.money, company.goods, len(company.employees), year])


def save_state_data(state, year):
    with open('./state.csv', mode='a') as state_file:
        state_writer = csv.writer(
            state_file,
            delimiter=',',
            quotechar='"',
            quoting=csv.QUOTE_MINIMAL
        )

        state_writer.writerow(
            [state.money, year])


def save_person_data(person, year):
    with open('./people.csv', mode='a') as population_file:
        population_writer = csv.writer(
            population_file,
            delimiter=',',
            quotechar='"',
            quoting=csv.QUOTE_MINIMAL
        )

        population_writer.writerow(
            [
                person.id,
                person.age,
                person.money,
                len(person.children),
                person.days_without_basic_needs,
                year
            ])
