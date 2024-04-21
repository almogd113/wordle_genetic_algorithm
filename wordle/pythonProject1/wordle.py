from genetic_classes.population import Population
from genetic_classes.genetic_algorithm import POPULATION_SIZE

def driver()-> None:
    population = Population(POPULATION_SIZE).init_population()

driver()