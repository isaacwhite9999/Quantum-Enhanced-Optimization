"""
Demonstrates how to adapt learning rates for quantum-classical hybrid optimization.
"""

import numpy as np

def adaptive_learning_rate(step, base_lr=0.1, decay=0.01):
    """
    Simple example: LR(t) = base_lr / (1 + decay*t)
    """
    return base_lr / (1.0 + decay*step)

def update_params(params, grads, step):
    """
    Updates parameter vector given gradients and an adaptive LR schedule.
    """
    lr = adaptive_learning_rate(step)
    new_params = [p - lr*g for p, g in zip(params, grads)]
    return new_params, lr

def run_learning_rate_adaptation(initial_params=[0.0, 0.0], steps=5):
    """
    Minimal demonstration of parameter updates using the schedule above.
    """
    params = initial_params
    for s in range(steps):
        # Suppose our gradient is random
        grads = np.random.randn(len(params)) * 0.1
        params, lr = update_params(params, grads, s)
    return params
