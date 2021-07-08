# World Wealth Multi-agent Simulation

## Agent

### Atributes:

- id - Unique identifier
- age
- money
- children - list with all children
- Dead Age - Maximum age that a agent will have
- Days Without Eat - Consequetive days without fill the basic needs. (If greater than 3, the person will die)
- Genes - Characteristics that are select at random, in born:
  - Study - If True Person will study after legal age
  - Spend Money - Percentage of money that the person will spend in other needs than the basic
  - Baby - If True person will have children
  - Premature die - If True person will die before 'Dead Age'
  - Invest - If True person will invest some percentage of this money
- Invest Percentage - percentage of money that a person will invest each year. Sampled from uniform distribution between 0.05 and 0.2
- Years to give birth - Years at person will give birth. Sampled from a geometric distribution.
- Year of Premature Dead - Year that a person will die prematurely. Sampled from a normal distribution with mean:30 and std 25

### Methods

- have_money - Check if person have money to spend.
- work - If person have more than legal age and don't study, increase this money by the SALARY, define in settings. If person study and have more than the age needed for work, increase this money by SALARY\*STUDY_COMPENSATION_GAIN (STUDY_COMPENSATION_GAIN >= 1)

- basic_needs - Remove from person money the money needed for basic needs for survive

- other_needs - If person works, remove from person money the amount spended in other needs than the basic, value calculated whir
