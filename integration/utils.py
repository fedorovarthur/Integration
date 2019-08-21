from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from typing import Any, Callable

import integration.config as config

# Decorator to allow tail recursion
class recursion(object):
    func: Callable

    def __init__(self, func: Callable):
        self.func = func

    def __call__(self, *args, **kwargs) -> Any:
        result = self.func(*args, **kwargs)
        while callable(result):
            result = result()
        return result

    def call(self, *args, **kwargs) -> Callable:
        return lambda: self.func(*args, **kwargs)


@recursion
def recursive_adaptation(f: Callable, x1: float, x2: float) -> float:
    y1, y2 = f(x1), f(x2)
    xm = (x1 + x2) / 2
    ym = f(xm)

    area12 = (x2 - x1) * (y1 + y2) / 2
    area1m2 = ((xm - x1) * (y1 + ym) + (x2 - xm) * (ym + y2)) / 2

    if abs((area1m2 - area12) / area12) < config.epsilon:
        return area1m2
    else:
        return recursive_adaptation(f, x1, xm) + recursive_adaptation(f, xm, x2)
