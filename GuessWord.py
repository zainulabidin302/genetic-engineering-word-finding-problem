import random


class Chromosome:
    def __init__(self, genes):
        self.Genes = genes
        self.Fitness = get_fitness(self)
        self.RelativeFitness =0

def generate_individual(length, geneSet):
    genes = []
    while (len(genes) < length):
        sampleSize = min(length - len(genes), len(geneSet))
        # print(sampleSize)
        genes.extend(random.sample(geneSet,sampleSize))

    genes = ''.join(genes)
    return Chromosome(genes)


def get_fitness2(chrom):
    guess = chrom.Genes
    return sum(1 for expected, actual in zip(word,guess) if expected == actual)

def get_fitness(chrom):
    guess = chrom.Genes
    return (sum(1 for actual in guess if word.find(actual)>-1)*2+ sum(1 for expected, actual in zip(word,guess) if expected == actual)*10)


def mutate(chromosome, mutation_chance=0.1):
    if random.random()<=mutation_chance:
        index = random.randrange(0,len(chromosome.Genes))
        randNo = random.randrange(0,len(geneSet))
        # print('lenthg of chromosome: ', len(chromosome.Genes))
        chromosome.Genes= chromosome.Genes.replace(chromosome.Genes[index],geneSet[randNo])
    return chromosome



def crossover (chrom1, chrom2, co_chance=0.7):
     if random.random()<=co_chance:
        temp = chrom1.Genes[4:8]
       # print(chrom1.Genes[4:8])
        chrom1.Genes=chrom1.Genes.replace(chrom1.Genes[4:8], chrom2.Genes[4:8])
        chrom2.Genes=chrom2.Genes.replace(chrom2.Genes[4:8], temp)
     return chrom1
    #return (chrom1, chrom2)



def selection_step(sorted_old_population):
    # def select_one():
    #     while True:
    #         candidate_idx = random.randint(0,len(sorted_old_population)-1)
    #         if random.randint(0,len(sorted_old_population))>= candidate_idx:
    #             return sorted_old_population[candidate_idx]
    #selections = [select_one(),select_one()]
    selections = [selectIndividual(sorted_old_population),selectIndividual(sorted_old_population)]
    while selections[1] == selections[0]:
        selections[1] = selectIndividual(sorted_old_population)
    return selections

def selectIndividual(population):
    max = sum(chromosome.Fitness for chromosome in population)
    pick = random.uniform(0, max)
    current = 0
    for chromosome in population:
        current += chromosome.Fitness
        if current > pick:
            return chromosome

def create_new_population(old_population,elitism=0):
    sorted_population = sorted(old_population,key= get_fitness,reverse=True)
    print ("BEST OLD:",sorted_population[0],get_fitness(sorted_population[0]))
    new_population = sorted_population[:elitism]
    while len(new_population) < size_of_population:
        crossOvered = crossover(*selection_step(sorted_population))
        mutated = mutate(crossOvered)
        new_population.append(mutated)
    calculate_relative_fitness(new_population[:size_of_population])
    return new_population[:size_of_population]

def calculate_relative_fitness(population):
    total_fitness = sum(get_fitness(i) for i in population)
    for ind in population:
        ind.RelativeFitness = (ind.Fitness/(total_fitness+1))*100





######################################################################
geneSet = "abcdedfghijklmnopqrstuvwxyz"
word = "artificial"
optimalFitness = len(word)
size_of_population = 100
best_solution=generate_individual(len(word), geneSet)
n_generations = 1000


population = [generate_individual(optimalFitness,geneSet) for _ in range(size_of_population)]
best_solution = population[0].Fitness
for i in range(n_generations):
    print("Generation No. ",i)
    population = create_new_population(population,3)
    maxS= max(indiv.Fitness for indiv in population)
    print("Max Fitness: ", maxS)
    if best_solution< maxS:
        best_solution=maxS
   # best_solution = population.index(max(indiv.Fitness for indiv in population))
#    if population[0].Fitness > best_solution.Fitness:
#        best_solution = population[0]
#    print("Overall Best so far",best_solution)


