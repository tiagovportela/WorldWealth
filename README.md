# World Wealth Multi-agent Simulation

## Agent

### Atributes:

- id - Unique identifier
- age
- money
- children - list with all children
- dead_age - Maximum age that a agent will have
- days_without_eat - Consequetive days without fill the basic needs. (If greater than 3, the person will die)
- alive - True if person alive, False otherwise
- genes - Dictionary with characteristics that are select at random, in born:
  - study - If True Person will study after legal age
  - spend money - Percentage of money that the person will spend in other needs than the basic
  - baby - If True person will have children
  - premature die - If True person will die before 'dead_age'
  - invest - If True person will invest some percentage of this money
- invest_percentage - percentage of money that a person will invest each year. Sampled from uniform distribution between 0.05 and 0.2
- years_to_give_birth - Years at person will give birth. Sampled from a geometric distribution.
- year_premature_die - Year that a person will die prematurely. Sampled from a normal distribution with mean:30 and std 25

### Methods

- have_money - Check if person have money to spend.
- work - If person have more than legal age and don't study, increase this money by the SALARY, define in settings. If person study and have more than the age needed for work, increase this money by SALARY\*STUDY_COMPENSATION_GAIN (STUDY_COMPENSATION_GAIN >= 1)

- basic_needs - Remove from person money the money needed for basic needs for survive

- other_needs - If person works, remove from person money the amount spended in other needs than the basic, value calculated based on person genes.

- feed_children - If have children and they don't work, increase ther money with FEED_CHILD, defined in settings

- invest - If person work and have in ther genes the gene to invest, increase is money by the amount defined by INTEREST_RATE and the percenge of money invested

- make_baby - If person have the gene baby create a person and add it to world population, and children list

- dead - Check if person arrive to the age of deying or have 3 days at lest witout providing the basic needs, if true change is alive state to False and give his money to ther chindren evenly.
