import pytest
from learning_rate_adaptation import run_learning_rate_adaptation

def test_run_learning_rate_adaptation():
    final_params = run_learning_rate_adaptation()
    assert len(final_params) == 2
