crossover_rate = 1
mutation_rate = 0.8
base_population = 20
pop_sample = 5
fitness_history = []


# UTIL

def argsort(seq):
    return sorted(range(len(seq)), key=seq.__getitem__)


def verify_condition(pupulation):
    return 0 in pupulation


def get_best_solution(population_fit):
    count = 0
    aux = 100
    for i in range(len(population_fit)):
        if population_fit[i] < aux:
            aux = population_fit[i]
            count = i
    return count


def draw_pop(pop):
    for i in range(len(pop)):
        line = ''.format((8-i), ' ')
        for j in range(len(pop)):
            if pop[j] == i:
                line = line + "X "
            else:
                line = line + "- "
        print(line)


def fitness_nq(solution):
    xeques = 0
    for i in range(0,len(solution)):
        for j in range(0,len(solution)):
            if i!=j:
                if i-solution[i] == j-solution[j] or i+solution[i] == j+solution[j]:
                    xeques+=1
    return xeques
