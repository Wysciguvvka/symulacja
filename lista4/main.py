import math
import random
from scipy.special import comb


def uniform_dist():
    sigma = 0.16
    mi = 3
    return sigma * math.sqrt(3) * (2 * random.uniform(0, 1) - 1) + mi


def z1():
    # N = 1000
    b = 300
    c = 0
    cs = []
    total = []
    for i in range(111):  # dla >110 przedmiotow 0%
        hits = 0
        for itr in range(100):  # powtorzenia losowania
            total_wage = sum([uniform_dist() for _ in range(i)])
            hits += 1 if total_wage <= b else 0  # suma < plecak
        cmb = comb(1000, i, exact=True)
        calc = hits / 100 * cmb  # ilosc trafien/proby * (ilosc kombinacji)

        cs.append(calc)
        total.append(cmb)
        c += calc

    # print([x[0] / x[1] for x in zip(cs, total)])
    # print(cs)
    # print(total)
    print('z1')
    print(f'średnia ilośc rozwiązań: 2^{math.log(c, 2)}')


def z2():
    # e^-x^2/2 0-1
    def gaussian(_x):
        return math.exp(-_x ** 2 / 2)

    k = 0
    n = 1000
    for i in range(n):
        y = random.uniform(0, 1)
        x = random.uniform(0, 1)
        if y < gaussian(x):
            k += 1
    p = k/n * 1
    print('----\nz2')
    print(f'Całka obliczona z pola kwadratu: {p}')
    fx = []
    for i in range(n):
        fx.append(gaussian(random.uniform(0,1)))
    area = (1-0)/n * sum(fx)
    print(f'Całka obliczona ze średniej: {area}')

z1()
z2()
