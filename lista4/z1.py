import math
from math import sqrt, floor
from random import uniform, getrandbits
from scipy.special import comb
from numpy import array
c = 0
cs = []
total = []
f_inverse = lambda: sigma * sqrt(3) * (2 * uniform(0, 1) - 1) + mi
for i in range(111):  # ilosc przedmiotow pakowanych
    hits = 0
    for itr in range(100):  # powtorzenia losowania
        total_wage = sum([f_inverse() for _ in range(i)])
        hits += 1 if total_wage <= 300 else 0  # suma < plecak
    cmb = comb(1000, i, exact=True)
    calc = hits / 100 * cmb  # ilosc trafien/proby * (ilosc kombinacji)

    cs.append(calc)
    total.append(cmb)
    c += calc
print([x[0] / x[1] for x in zip(cs, total)])
print(cs)
print(total)