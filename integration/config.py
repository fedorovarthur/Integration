import integration.methods as methods

methods_slice = {
    'rectangle': methods.rectangle_slice,
    'trapezoid': methods.trapezoid_slice,
    'adaptive': methods.adaptive_slice,
    'simpson': methods.simpson_slice,
    'monte_carlo': methods.monte_carlo_slice
}

epsilon = 10e-8