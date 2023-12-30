import random

import MainEq
from Member import Member


# noghteie
def recombination(v1, v2):
    rand = random.randint(1, 4)
    offspring = []
    for i in range(0, rand):
        offspring.append(v1[i])
    for i in range(rand, 5):
        offspring.append(v2[i])

    member = Member(offspring, fitness= MainEq.fitness(offspring))
    member.fitness = MainEq.fitness(member.arr)
    print(member.fitness)
    return Member


recombination([-1/2, 0, 1/3, 0, 0], [-1/7, 0, 1/3, 0, 0])
