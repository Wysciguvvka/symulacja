import matplotlib.pyplot as plt


def avg(data: list) -> float:
    return sum(data) / len(data)


def kosci(n: int = 30) -> dict:
    from lista1 import RandGen
    p1_score = [RandGen.randint(1, 6) + RandGen.randint(1, 6) for _ in range(n)]
    p2_score = [RandGen.randint(1, 6) + RandGen.randint(1, 6) for _ in range(n)]
    p1_data = {'wyniki': [], 'przewagi': []}
    for p1, p2 in zip(p1_score, p2_score):
        p1_data['wyniki'].append(p1)
        p1_data['przewagi'].append(p1 - p2)

    return p1_data


def kosci2(n: int = 30) -> dict:
    from lista1 import RandGen
    p1_score = []
    p2_score = []
    p1_data = {'wyniki': [], 'przewagi': []}
    for _ in range(n):
        p1_score.append(RandGen.randint(1, 6) + RandGen.randint(1, 6))
        p2_score.append(RandGen.randint(1, 6) + RandGen.randint(1, 6))
    for p1, p2 in zip(p1_score, p2_score):
        p1_data['wyniki'].append(p1)
        p1_data['przewagi'].append(p1 - p2)
    return p1_data


if __name__ == '__main__':
    gra = kosci2()
    print(gra)
    print(avg(gra['wyniki']))
    print(avg(gra['przewagi']))

    fig, axs = plt.subplots(2)

    axs[0].set_title("Rozkład wyników Gracza1")
    axs[0].hist(gra['wyniki'], bins=range(2, 13), linewidth=0.5, edgecolor='black')
    axs[0].set_xticks(range(2, 13))
    axs[0].set_xlabel("Wynik")
    axs[0].set_ylabel("Ilość powtórzeń")

    axs[1].set_title("Rozkład przewag Gracza1")
    axs[1].hist(gra['przewagi'], bins=range(-10, 11), linewidth=0.5, edgecolor='black')
    axs[1].set_xticks(range(-10, 11))
    axs[1].set_xlabel("Przewaga")
    axs[1].set_ylabel("Ilość powtórzeń")

    plt.tight_layout()
    plt.show()
