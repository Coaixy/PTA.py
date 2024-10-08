import numpy as np


def sigmoid(a):
    return 1 / (1 + np.exp(-a))

a = int(input())
print(f"{sigmoid(a):.2f}")