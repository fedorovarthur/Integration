import random

class Integration():
    
    def __init__(self, f, a, b, numIntervals = 1000, method = 'adaptive'):
        '''
        Minimalistic class for function integration with four methods.
        
        Inputs:
        Callable: f - function to integrate over
        Int: a - lower bound
        Int: b - upper bound
        Int: numIntervals - num of intervals or random samples
        String: method - specified method of integration
        
        Outputs:
        Double: area - area under the function
        '''
        self.f_ = f
        self.a_ = a
        self.b_ = b
        self.numIntervals_ = numIntervals
        self.method_ = method
        self._dX = (b - a)/numIntervals
        self.area = .0
    
    def _rectangleMethod(self):
        x = self.a_
        for i in range(self.numIntervals_):
            self.area += self._dX*self.f_(x)
            x += self._dX
        return self.area
    
    def _trapezoidMethod(self):
        x = self.a_
        for i in range(self.numIntervals_):
            self.area += self._dX*(self.f_(x) + self.f_(x + self._dX))/2
            x += self._dX
        return self.area
    
    def _adaptiveMethod(self):
        x = self.a_
        for i in range(self.numIntervals_):
            self.area += self._sliceArea(x, x + self._dX)
            x += self._dX
        return self.area
        
    def _sliceArea(self, x1, x2):
        y1 = self.f_(x1)
        y2 = self.f_(x2)
        xm = (x1 + x2)/2
        ym = self.f_(xm)
        
        area12 = (x2 - x1)*(y1 + y2)/2
        area1m2 = ((xm - x1)*(y1 + ym) + (x2 - xm)*(ym + y2))/2
        
        #TODO: add error term as hyperparameter
        if abs((area1m2 - area12)/area12) < 10e-4:
            return area1m2
        else:
            return self._sliceArea(x1, xm) + self._sliceArea(xm, x2)
    
    def _monteCarloMethod(self):
        #TODO: add random seed as hyperparameter
        for iter in range(self.numIntervals_):
            self.area += self._dX*self.f_(random.uniform(self.a_, self.b_))
        return self.area
        
    def solve(self):
        if self.method_ in ['rectangle', 'trapezoid', 'adaptive', 'monte-carlo']:

            try:
                assert self.area == .0
            except:
                self.area = .0

            if self.method_ == 'rectangle':
                return self._rectangleMethod()
            elif self.method_ == 'trapezoid':
                return self._trapezoidMethod()
            elif self.method_ == 'adaptive':
                return self._adaptiveMethod()
            else:
                return self._monteCarloMethod()
                
        else:
            raise ValueError('Unsupported method, try rectangle, trapezoid, adaptive or monte-carlo')