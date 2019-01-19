from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from random import uniform

from numba import jit

from integration.utils import recursive_adaptation


@jit(fastmath=True, parallel=True)
def apply_method(f, a, dx, n, slice_area):
    area = 0
    x = a
    for interval in range(n):
        area += slice_area(f, x, dx)
        x += dx
    return area


def rectangle_slice(f, x, dx):
    return dx * f(x)


def trapezoid_slice(f, x, dx):
    return dx * (f(x) + f(x + dx))/2


def adaptive_slice(f, x, dx):
    return recursive_adaptation(f, x, x + dx)


def simpson_slice(f, x, dx):
    return dx/6 * (f(x) + 4 * f(x + dx/2) + f(x + dx))


def monte_carlo_slice(f, x, dx):
    return dx * f(uniform(x, x + dx))


config = {'rectangle': rectangle_slice, 'trapezoid': trapezoid_slice, 'adaptive': adaptive_slice,
          'simpson': simpson_slice, 'monte_carlo': monte_carlo_slice}
