from population import Population
from genetic_algorithm import POPULATION_SIZE

def driver()-> None:
    population = Population(POPULATION_SIZE).init_population()

driver()