from population import Population

TARGET_CHROMOSOME = "almog"
POPULATION_SIZE = 8


def crossover_population(population: Population) -> Population:
    return population


def mutate_population(population: Population) -> Population:
    return population


def evolve(population: Population) -> Population:
    return mutate_population(crossover_population(population))
