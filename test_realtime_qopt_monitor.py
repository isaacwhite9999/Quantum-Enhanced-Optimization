import pytest
from realtime_qopt_monitor import run_realtime_monitor_simulation

def test_run_realtime_monitor_simulation():
    history = run_realtime_monitor_simulation(steps=3)
    assert len(history) == 3
