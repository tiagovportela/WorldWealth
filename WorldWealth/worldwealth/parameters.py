# ------------ PERSON PARAMETERS ------------- #

# GENE dominance probablity

PROBABILITY_STUDY = [0.2, 0.8]
PROBABILITY_HAVE_CHILDREN = [0.65, 0.35]
PROBABILITY_P_DEATH = [0.01, 0.99]
PROBABILITY_INVEST = [1.0, 0.0]
PROBABILITY_WORK_SECTOR = [0.3, 0.6, 0.1]
#SPEND_MONEY_PERCENTAGE = [0.05, 0.2, 0.7, 0.9]
SPEND_MONEY_PERCENTAGE = [0.05, 0.5, 0.9]


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

# age range that age concider a premature death
P_DEATH_RANGE = (0, 60)


# Parameters for calculate age of death
# sample from a normal distribution
MEAN_DEATH = 85
STD_DEATH = 20

# age range that age consider a normal dead
DEATH_RANGE = (0, 100)

# Miminum money earn by working
YEAR_INCOME = 30_000
# Compensation for study, value must be greater or equal to 1
STUDY_COMPENSATION_GAIN = 1.3

# Amount of money need for meet the basic needs of adult person
BASIC_NEEDS_ADULT = 0.1*YEAR_INCOME

# Amount of money need for meet the basic needs of child
BASIC_NEEDS_CHILD = 0.05*YEAR_INCOME

# Amount that a parent give to her child
FEED_CHILD = 0.05*YEAR_INCOME

WORKING_AGE = 27
RETIREMENT_AGE = 65
LEGAL_AGE = 18

INTEREST_RATE = 0.05


MAX_DAYS_WITHOUT_BASIC_NEEDS = 3

#-------------------------------------------#
# ------------ STATE PARAMETERS ------------#

BASE_TAX = 0.03

# When money go to state,
STATE_EFFIENCY = 0.1

VAT_TAX = 0.15

IRC_TAX = 0.35
# Disponibility for spend money defined by a tutle
# first element is lower limit, second higher limit
# third is the gain

WEALTH_RANKS = {
    'FIRST': (4, 6, 1.2),
    'SECOND': (7, 8, 1.3),
    'THIRD': (8, 9, 1.5),
    'FOURTH': (9, 10, 1.7),
    'FIFTH': (11, '-', 2.3)
}

#-------------------------------------------#
# ------------ COMPANIES PARAMETERS ------------#

VALUE_ADD = 6.5
# RESOURCES_TO_MAKE_A_PRODUCT =
NUMBER_PRODUTS_MADE_BY_EMPLOYEE = 3

#-------------------------------------------#
# ------------ WORLD PARAMETERS ------------#
BASE_RESOURCES = 500
