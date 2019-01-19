from sklearn.base import BaseEstimator

from .methods import config


class BaseIntegrator(BaseEstimator):

    def __init__(self, n_intervals, method):
        assert method.lower() in config.keys(), f'Inappropriate method, try: {config.keys()}'
        self.n_intervals = n_intervals
        self.method = method

    @staticmethod
    def _find_method(method):
        return config[method]

    def fit(self, a, b):
        self.dx_ = (b - a)/self.n_intervals
        self.method_ = self._find_method(self.method)
