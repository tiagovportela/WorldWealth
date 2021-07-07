import numpy as np

from settings import *


# return a list with years that a person will give birth
# the list is sampled from a geometric distribution
def bird_age():
    bird_age = list()
    start, end = FERTILE_YEARS
    range_birth = end - start
    while len(bird_age) < NUMBER_OF_CHILDREN:
        value = np.random.geometric(p=1/16, size=1)[0]
        if value <= range_birth:
            value += start
            if value not in bird_age:
                bird_age.append(value)

    return bird_age
