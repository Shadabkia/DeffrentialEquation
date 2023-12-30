from numpy import random

# DifferentialEquation
# Equation: y'- 1/2y - x^4/16 + x^3/2 + x^2/4 - x = 0
# Condition : y(0) = 0 , 0<x<1 interval 0.1
# Exact solution :  y = -1/8x^4 + 1/2x^2

# y' = 4ax3 + 3mx2 + 2bx + c
# y = ax4 + mx3 + bx2 + cx + d,
# y' - 1/2y = -a/2x4 + (8a-m)/2x3 + (6m-b)/2x2 + (4b-c)/2x + c-d/2
import numpy.random as npr

from Member import Member

eps = 10 ** -16
step = 0.1
weight = 10
n_population = 10
loop = 1000
populationArr = []
population = []


def R(x, a, m, b, c, d): return -(8 * a + 1) / 16 * x ** 4 + (8 * a - m + 1) / 2 * x ** 3 + (
        12 * m - 2 * b + 1) / 4 * x ** 2 + (4 * b - c - 2) / 2 * x + c - d / 2


def R2(d): return d


def sumR(arr):
    my_sum = 0
    for i in range(1, 11):
        my_sum += abs(R(i * step, arr[0], arr[1], arr[2], arr[3], arr[4]))
    return my_sum + abs(weight * R2(arr[4]))


# 0 <= x <= 1, step 0.1
def fitness(arr):
    return 1 / (sumR(arr) + R2(arr[4]) + eps)


def initPopulation(n):
    populationArr = random.normal(size=(n, 5))
    for i in range(0, n):
        member = Member(populationArr[i], fitness(populationArr[i]))
        population.append(member)


def selectOne(population):
    my_max = sum([c.fitness for c in population])
    selection_probs = [c.fitness / my_max for c in population]
    return population[npr.choice(len(population), p=selection_probs)]


for i in population:
    print(i.fitness)

initPopulation(n_population)
print(random.normal(size=(n_population, 5)))
print(selectOne(population).fitness)
