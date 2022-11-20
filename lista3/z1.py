import math
import random
import matplotlib.pyplot as plt
import numpy as np


# ???
def gen_z1(half_life: int | float) -> list:
    _lambda = math.log(2) / half_life  # ln
    # normalizacja - lambda = ln(2)/hl
    # p(t) = e^-(lambda*t) [0-inf) - p-stwo ze czastka przetrwa tyle czasu
    # 1 - p(t) - p-stwo ze sie rozpadnie
    # t = random.uniform(0, float('inf'))
    # F^-1(t) = -ln(1-t)/lambda
    sample = []
    for _ in range(10000):
        prob = random.uniform(0, 1)
        sample.append(-math.log(prob) / _lambda)
    return sample


def z1(half_life: int | float) -> list[int]:
    # 3561 lat
    # f(t) = lambda*e^-(lambda*t)
    # F(t) = 1-e^(-lambda*t)
    _lambda = math.log(2) / half_life  # ln
    data: list[int] = []
    for i in range(20000):
        t = y = x = 0
        while not y < x:
            t = random.randint(0, 51000)
            x = _lambda * math.exp(-_lambda * t)
            y = random.uniform(0, _lambda)
        data.append(t)
    return data


if __name__ == '__main__':
    dist = z1(5730)
    dist_normalized = [s*math.log(2)/5370 for s in dist]
    bins_count = 100
    scaled_data = np.histogram(dist, bins=bins_count, density=True)
    counts, bins = scaled_data[1], (scaled_data[0] * 5730 / math.log(2))
    plt.bar(counts[:-1], bins, 51000 / bins_count)
    plt.ylabel('p-stwo')
    plt.xlabel('czas')
    plt.show()
    plt.hist(dist_normalized, bins=30, density=True)
    plt.show()
    closest = min(zip(counts[:-1], bins), key=lambda x: abs(x[1] - 0.65))
    print(closest)
