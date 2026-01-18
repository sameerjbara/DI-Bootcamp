# Instructions :
# This challenge is about Biology that will put emphasis on your knowledge of classes, inheritance and polymorphism.

# Build a DNA object. DNA is composed of chromosomes which is itself composed of Genes.
# A Gene is a single value 0 or 1, it can mutate (flip).
# A Chromosome is a series of 10 Genes. It also can mutate, meaning a random number of genes can randomly flip (1/2 chance to flip).
# A DNA is a series of 10 chromosomes, and it can also mutate the same way Chromosomes can mutate.

# Implement these classes as you see fit.

# Create a new class called Organism that accepts a DNA object and an environment parameter that sets the probability for its DNA to mutate.

# Instantiate a number of Organism and let them mutate until one gets to a DNA which is only made of 1s. Then stop and record the number of generations (iterations) it took.
# Write your results in you personal biology research notebook and tell us your conclusion :).

import random


class Gene:
    def __init__(self, value=None):
        if value is None:
            value = random.randint(0, 1)
        if value not in (0, 1):
            raise ValueError("Gene value must be 0 or 1.")
        self.value = value

    def mutate(self):
        # flip 0 <-> 1
        self.value = 1 - self.value

    def __repr__(self):
        return str(self.value)


class Chromosome:
    LENGTH = 10

    def __init__(self, genes=None):
        if genes is None:
            self.genes = [Gene() for _ in range(self.LENGTH)]
        else:
            if len(genes) != self.LENGTH:
                raise ValueError(f"Chromosome must contain exactly {self.LENGTH} genes.")
            self.genes = genes

    def mutate(self):
        # random number of genes, each has 1/2 chance to flip
        k = random.randint(0, self.LENGTH)
        idxs = random.sample(range(self.LENGTH), k)
        for i in idxs:
            if random.random() < 0.5:
                self.genes[i].mutate()

    def is_all_ones(self):
        return all(g.value == 1 for g in self.genes)

    def __repr__(self):
        return "".join(str(g.value) for g in self.genes)


class DNA:
    LENGTH = 10

    def __init__(self, chromosomes=None):
        if chromosomes is None:
            self.chromosomes = [Chromosome() for _ in range(self.LENGTH)]
        else:
            if len(chromosomes) != self.LENGTH:
                raise ValueError(f"DNA must contain exactly {self.LENGTH} chromosomes.")
            self.chromosomes = chromosomes

    def mutate(self):
        # random number of chromosomes, each has 1/2 chance to mutate (which may flip genes)
        k = random.randint(0, self.LENGTH)
        idxs = random.sample(range(self.LENGTH), k)
        for i in idxs:
            if random.random() < 0.5:
                self.chromosomes[i].mutate()

    def is_all_ones(self):
        return all(ch.is_all_ones() for ch in self.chromosomes)

    def __repr__(self):
        return "\n".join(str(ch) for ch in self.chromosomes)


class Organism:
    def __init__(self, dna, environment):
        """
        dna: DNA object
        environment: probability [0..1] that DNA mutates per generation
        """
        if not isinstance(dna, DNA):
            raise TypeError("dna must be a DNA instance.")
        if not (0 <= environment <= 1):
            raise ValueError("environment must be a probability between 0 and 1.")
        self.dna = dna
        self.environment = environment

    def reproduce_next_generation(self):
        # In this simplified model, the organism continues with the same DNA object.
        # Each generation: environment decides whether DNA mutates.
        if random.random() < self.environment:
            self.dna.mutate()


def run_simulation(num_organisms=20, environment=0.2, max_generations=1_000_000):
    organisms = [Organism(DNA(), environment) for _ in range(num_organisms)]

    generation = 0
    while generation < max_generations:
        generation += 1

        for org in organisms:
            org.reproduce_next_generation()
            if org.dna.is_all_ones():
                return generation, org.dna  # success

    return None, None  # not found within limit


if __name__ == "__main__":
    generations, winning_dna = run_simulation(num_organisms=50, environment=0.3)

    if generations is None:
        print("No organism reached all 1s within the generation limit.")
    else:
        print(f"Success! An organism reached all 1s in {generations} generations.")
        print("Winning DNA:")
        print(winning_dna)
