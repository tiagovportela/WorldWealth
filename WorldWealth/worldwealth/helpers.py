import numpy as np

from .constants import *
from .parameters import *

# function that return the values for the genes


def gene(type):
    if type == STUDY:
        return np.random.choice(a=[True, False], p=PROBABILITY_STUDY)
    elif type == BABY:
        return np.random.choice(a=[True, False], p=PROBABILITY_HAVE_CHILDREN)
    elif type == P_DEATH:
        return np.random.choice(a=[True, False], p=PROBABILITY_P_DEATH)
    elif type == INVEST:
        return np.random.choice(a=[True, False], p=PROBABILITY_INVEST)
    elif type == S_MONEY:
        return np.random.choice(SPEND_MONEY_PERCENTAGE)

# return percentage of money that a person will invest
# sampled from a uniform distribution


def percentage_money_person_will_invest():
    return np.random.uniform(0.05, 0.2, size=1)[0]

# function that return the number of children that a person will have
# sample from normal distribution


def number_of_children_person_will_have():
    return abs(int(np.random.normal(MEAN_CHILDREN, STD_CHILDREN)))

# function that return the age at a person will give birth to the children
# Sample ages from normal distribution


def children_birth_age():

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

# Function that return the age of premature death.
# Age sample from a normal distribution


def age_premature_death():
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
    age = []
    min_age, max_age = DEATH_RANGE
    while(len(age) < 1):
        value = int(
            np.random.normal(loc=MEAN_DEATH, scale=STD_DEATH, size=1))
        if value > min_age and value < max_age:
            age.append(value)
    return age[0]
