# ------------ PERSON PARAMETERS ------------- #

# GENE dominance probablity

PROBABILITY_STUDY = [0.2, 0.8]
PROBABILITY_HAVE_CHILDREN = [0.5, 0.5]
PROBABILITY_P_DEATH = [0.01, 0.99]
PROBABILITY_INVEST = [1.0, 0.0]
SPEND_MONEY_PERCENTAGE = [0.05, 0.2, 0.7, 0.9]

# Parameters for calculate number of children
# sample from a normal distribution
MEAN_CHILDREN = 3
STD_CHILDREN = 2

# FERTILE YEARS RANGE
FERTILE_YEARS = (16, 45)

# Parameters for calculate age at a person will give birth to the children
# sample from a normal distribution
MEAN_BIRTH_CHILD_AGE = 33
STD_BIRTH_CHILD_AGE = 5

# Parameters for calculate age of premature  death
# sample from a normal distribution
MEAN_P_DEATH = 45
STD_P_DEATH = 15

# age range that age confider a premature dead
P_DEATH_RANGE = (0, 60)


# Parameters for calculate age of death
# sample from a normal distribution
MEAN_DEATH = 85
STD_DEATH = 20

# age range that age consider a normal dead
DEATH_RANGE = (0, 100)

# Miminum money earn by working
SALARY = 10_000
# Compensation for study, value must be greater or equal to 1
STUDY_COMPENSATION_GAIN = 1.3

# Amount of money need for meet the basic needs of adult person
BASIC_NEEDS_ADULT = 0.1*SALARY

# Amount of money need for meet the basic needs of child
BASIC_NEEDS_CHILD = 0.05*SALARY

# Amount that a parent give to her child
FEED_CHILD = 0.1*SALARY

WORKING_AGE = 27
RETIREMENT_AGE = 65
LEGAL_AGE = 18

INTEREST_RATE = 0.05


MAX_DAYS_WITHOUT_BASIC_NEEDS = 3

#-------------------------------------------#
# ------------ STATE PARAMETERS ------------#

BASE_TAX = 0.03
