from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


# Decorator to allow tail recursion
class recursion(object):

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)
        while callable(result): result = result()
        return result

    def call(self, *args, **kwargs):
        return lambda: self.func(*args, **kwargs)


@recursion
def recursive_adaptation(f, x1, x2):
    y1, y2 = f(x1), f(x2)
    xm = (x1 + x2) / 2
    ym = f(xm)

    area12 = (x2 - x1) * (y1 + y2) / 2
    area1m2 = ((xm - x1) * (y1 + ym) + (x2 - xm) * (ym + y2)) / 2

    if abs((area1m2 - area12) / area12) < 10e-8:
        return area1m2
    else:
        return recursive_adaptation(f, x1, xm) + recursive_adaptation(f, xm, x2)
