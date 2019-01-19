from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from .base import BaseIntegrator
from .methods import apply_method


class Integrator(BaseIntegrator):
    """
    Minimalistic class for function integration with variety of methods.

    Inputs:
    Callable: f - function to integrate over
    Int: a - lower bound
    Int: b - upper bound
    Int: n_intervals - num of intervals or random samples
    String: method - specified method of integration

    Outputs:
    Double: area - area under the function
    """
    def __init__(self, **kwargs):
        super(Integrator, self).__init__(**kwargs)

    def solve(self, f, a, b):
        self.fit(a, b)
        return apply_method(f, a, self.dx_, self.n_intervals, self.method_)
