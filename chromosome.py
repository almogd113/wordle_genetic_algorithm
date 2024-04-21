import random
import genetic_classes.genetic_algorithm


class Chromosome:
    VALID_GENES = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    VALID_GENES_LIST = list(VALID_GENES)
    is_fitness_changed = False

    def __init__(self):
        self.genes = [(str)]
        self.fitness = 0
        self.target_word_length = len(genetic_classes.genetic_algorithm.TARGET_CHROMOSOME)

    def genes_init(self) -> None:
        genes = []
        for x in range(self.target_word_length):
            genes.append(random.choice(self.VALID_GENES_LIST))
        self.genes = genes

    def calculate_fitness(self):
        fitness_count = 0
        target_chromosome = genetic_classes.genetic_algorithm.TARGET_CHROMOSOME
        for gene_target, gene_chromosome in zip(self.genes, target_chromosome):
            if gene_target == gene_chromosome:
                fitness_count += 1
        return fitness_count

    def get_genes(self) -> []:
        self.is_fitness_changed = True
        return self.genes

    def get_fitness(self) -> int:
        if self.is_fitness_changed:
            self.fitness = self.calculate_fitness()
            self.is_fitness_changed = False
        return self.fitness

    def genes_string(self) -> str:
        genes_str = ""
        for char in self.genes:
            genes_str += char
        return genes_str

    def chromosome_string(self) -> None:
        format_txt = "Genes: {}\tfitness: {}"
        print(format_txt.format(self.genes_string(), self.fitness))


def print_list(lst: []) -> None:
    for x in lst:
        print(x)


# print_list(Chromosome(5).)
print(Chromosome().chromosome_string())
