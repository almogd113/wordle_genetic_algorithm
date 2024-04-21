from genetic_classes.chromosome import Chromosome


class Population:
    def __init__(self, population_length: int):
        self.chromosomes = [(Chromosome)]
        self.population_length = population_length

    def init_population(self) -> None:
        # from genetic_classes.genetic_algorithm import TARGET_CHROMOSOME
        for index in range(self.population_length):
            # self.chromosomes.append(Chromosome(len(TARGET_CHROMOSOME).genes_init()))
            self.chromosomes.append(Chromosome().genes_init())
        self.sort_chromosome_by_fitness()



    # def sort_chromosome_by_fitness(self) -> None:
    #
    #     self.chromosomes.sort(key= lambda x: )

    # def print_population(self) -> None:
    #     for chromosome in self.chromosomes:
