class Integration():
    
    def __init__(self, numIntervals = 1000, method = 'adaptive'):
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
        self.numIntervals_ = numIntervals
        self.method_ = method
        self.area = .0
    
    def _rectangleMethod(self, f, a, dX):
        x = a
        for i in range(self.numIntervals_):
            self.area += dX*f(x)
            x += dX
        return self.area
    
    def _trapezoidMethod(self, f, a, dX):
        x = a
        for i in range(self.numIntervals_):
            self.area += dX*(f(x) + f(x + dX))/2
            x += dX
        return self.area
    
    def _adaptiveMethod(self, f, a, dX):
        x = a
        for i in range(self.numIntervals_):
            self.area += self._sliceArea(f, x, x + dX)
            x += dX
        return self.area
        
    def _sliceArea(self, f, x1, x2):
        y1 = f(x1)
        y2 = f(x2)
        xm = (x1 + x2)/2
        ym = f(xm)
        
        area12 = (x2 - x1)*(y1 + y2)/2
        area1m2 = ((xm - x1)*(y1 + ym) + (x2 - xm)*(ym + y2))/2
        
        #TODO: add error term as hyperparameter
        if abs((area1m2 - area12)/area12) < 10e-4:
            return area1m2
        else:
            return self._sliceArea(x1, xm) + self._sliceArea(xm, x2)
    
    def _monteCarloMethod(self, f, a, b, dX):
        from random import uniform
        #TODO: add random seed as hyperparameter
        for iter in range(self.numIntervals_):
            self.area += dX*f(uniform(a, b))
        return self.area
        
    def solve(self, f, a, b):
        if self.method_ in ['rectangle', 'trapezoid', 'adaptive', 'monte-carlo']:

            try:
                assert self.area == .0
            except:
                self.area = .0
                
            self.f_ = f
            self.a_ = a
            self.b_ = b
            self._dX = (self.b_ - self.a_)/self.numIntervals_

            if self.method_ == 'rectangle':
                return self._rectangleMethod(self.f_, self.a_, self._dX)
            elif self.method_ == 'trapezoid':
                return self._trapezoidMethod(self.f_, self.a_, self._dX)
            elif self.method_ == 'adaptive':
                return self._adaptiveMethod(self.f_, self.a_, self._dX)
            else:
                return self._monteCarloMethod(self.f_, self.a_, self.b_, self._dX)
                
        else:
            raise ValueError('Unsupported method, try rectangle, trapezoid, adaptive or monte-carlo')