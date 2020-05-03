import integration.methods as methods

EPSILON = 10e-8

methods_slice = {
    'rectangle': methods.rectangle_slice,
    'trapezoid': methods.trapezoid_slice,
    'adaptive': methods.adaptive_slice,
    'simpson': methods.simpson_slice,
    'monte_carlo': methods.monte_carlo_slice
}
