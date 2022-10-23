import math
import matplotlib.pyplot as plt
from lista1 import RandGen


def archery(rounds: int = 10, size: int = 1220) -> dict:
    archer1_data = {'scores': [], 'points': [], 'distances': []}
    archer2_data = {'scores': [], 'points': [], 'distances': []}
    for _ in range(rounds):
        archer1_score, archer2_score = 0, 0
        radius = size * 0.5

        # archer1
        dist = RandGen.randint(-1000, 1000)  # (0, 1000)
        angle = RandGen.uniform_range(0, 2 * math.pi)
        x, y = dist * math.cos(angle), dist * math.sin(angle)
        archer1_score += 1 if abs(dist) <= radius else 0

        archer1_data['points'].append((x, y))
        archer1_data['scores'].append(archer1_score)
        archer1_data['distances'].append(abs(dist))

        # archer2
        x, y = RandGen.randint(-900, 900), RandGen.randint(-900, 900)
        dist = math.sqrt(x ** 2 + y ** 2)
        archer2_score += 1 if dist <= radius else 0

        archer2_data['points'].append((x, y))
        archer2_data['scores'].append(archer2_score)
        archer2_data['distances'].append(dist)

    archers_data = {'archer1': archer1_data, 'archer2': archer2_data}
    return archers_data


if __name__ == '__main__':
    import numpy as np

    fig, ax = plt.subplots()
    points_archer1 = []
    points_archer2 = []
    dists_archer1 = []
    dists_archer2 = []
    score_archer1 = 0
    score_archer2 = 0
    for _ in range(20):
        result = archery()
        dists_archer1 += result['archer1']['distances']
        dists_archer2 += result['archer2']['distances']
        points_archer1 += result['archer2']['points']
        points_archer2 += result['archer1']['points']
        score_archer1 += sum(result['archer1']['scores'])
        score_archer2 += sum(result['archer2']['scores'])

    print(sum(dists_archer2) / len(dists_archer2))  # 500 * sqrt(2)
    print(sum(dists_archer1) / len(dists_archer1))  # 500
    print('---')
    print(score_archer1, score_archer2)

    ax.scatter(*zip(*points_archer2), alpha=0.5)
    ax.scatter(*zip(*points_archer1), alpha=0.5)
    ax.set_xticks(np.arange(-1000, 1001, 250))
    ax.set_yticks(np.arange(-1000, 1001, 250))
    target = plt.Circle((0, 0), 660, color='green', fill=False, linewidth=2.5)
    ax.add_patch(target)
    ax.set_aspect('equal', adjustable='box')
    plt.tight_layout()
    plt.show()
