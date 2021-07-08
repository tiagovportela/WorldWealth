# World Wealth Multi-agent Simulation

## Agent

### Attributes:

- id - Unique identifier
- age
- money
- children - list of all children
- dead_age - Maximum age that an agent will be
- days_without_eat - Consecutive days without meeting basic needs. (If greater than 3 the person will die)
- alive - True if person alive, False otherwise
- genes - Dictionary with characteristics that are randomly selected at birth:
  - study - If True Person is going to study after legal age
  - spend money - Percentage of money the person will spend on needs other than basic
  - baby - If True person will have children
  - premature death - If True person will die before 'dead_age'
  - invest - If True, the person will invest some percentage of their money
- invest_percentage - percentage of the money a person will invest each year. Sampled from uniform distribution between 0.05 and 0.2
- years_to_give_birth - Years in which the person will give birth. Sampled from a geometric distribution.
- year_premature_death - Year in which a person will die prematurely. Sampled from a normal distribution with mean: 30 and std 25

### Methods

- have_money - Check if the person has money to spend.
- work - If the person is over the legal age and does not study, increase this money by SALARY, define in the settings. If the person studies and is older than the age necessary to work, increase this money by SALARY \* STUDY_COMPENSATION_GAIN (STUDY_COMPENSATION_GAIN> = 1)

- basic_needs - Take from the person's money the money needed for basic survival needs

- other_needs - If the person works, it takes from the person's money the amount spent on needs other than basic needs, calculated based on the person's genes.

- feed_children - If a Person have children and they don't work, raise their money with FEED_CHILD, defined in the settings

- invest - If the person works and has the gene to invest in his genes, Increase his money by the value defined by INTEREST*RATE * invest*percentage * money

- make_baby - If the person has the baby gene, create a person and add them to the world population and children list

- dead - Check if the person reaches the dead_age/year_premature_death or has at least 3 days without meeting basic needs, if True gives his money to children, equally distributed and change alive state to False.
