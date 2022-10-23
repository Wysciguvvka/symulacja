from __future__ import annotations
from datetime import datetime
import math


class RandGen:
    seed = int(datetime.now().timestamp() * 10009)
    x = seed
    a = 22695477
    c = 1
    m = 2 ** 32

    @classmethod
    def set_seed(cls, seed: int) -> None:
        cls.seed = seed
        cls.x = seed

    @classmethod
    def random(cls) -> int:
        cls.x = (cls.a * cls.x + cls.c) % cls.m
        return cls.x

    @classmethod
    def uniform(cls) -> float:
        # [0, 1)
        return cls.random() / cls.m

    @classmethod
    def uniform_range(cls, a: float, b: float) -> float:
        # [a, b)
        return (b - a) * cls.uniform() + a

    @classmethod
    def randint(cls, a: int, b: int) -> int:
        # [a, b]
        return math.floor(abs(b - a + 1) * cls.uniform() + a)
