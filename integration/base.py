from sklearn.base import BaseEstimator

from integration.config import methods_slice


class BaseIntegrator(BaseEstimator):

    def __init__(self, n_intervals: int, method: str):
        assert method.lower() in methods_slice.keys(), f'Inappropriate method, try: {methods_slice.keys()}'
        self.n_intervals = n_intervals
        self.method = method

    @staticmethod
    def _find_method(method: str):
        return methods_slice[method]

    def fit(self, a: int, b: int):
        self.dx_ = (b - a) / self.n_intervals
        self.method_ = self._find_method(self.method)
        self.area_ = 0
