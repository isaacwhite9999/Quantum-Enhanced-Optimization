"""
Enables real-time monitoring of quantum optimization metrics like cost, parameter values, etc.
"""

import numpy as np

class RealtimeOptimizerMonitor:
    def __init__(self):
        self.history = []

    def log_step(self, step, params, cost):
        """
        Stores step info in an internal history for potential real-time visualization.
        """
        self.history.append({"step": step, "params": params, "cost": cost})

    def current_snapshot(self):
        """Returns the last recorded step details."""
        if self.history:
            return self.history[-1]
        return None

def run_realtime_monitor_simulation(steps=5):
    """
    Demonstrates logging random cost/params at each step.
    """
    monitor = RealtimeOptimizerMonitor()
    params = [0.0, 1.0]
    for s in range(steps):
        cost = np.random.rand()
        monitor.log_step(s, params, cost)
        # simulate param update
        params = [p + 0.01 for p in params]
    return monitor.history
