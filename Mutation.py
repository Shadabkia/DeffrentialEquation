import numpy as np


def mutate(child, mutation_rate=0.3):
    if np.random.random() < mutation_rate:
        index = np.random.choice(5)
        child[index] += np.random.uniform(-0.2, 0.5)

    return child


print(mutate([-1, 0.02, 0.03, 0.04, 0.05]))
