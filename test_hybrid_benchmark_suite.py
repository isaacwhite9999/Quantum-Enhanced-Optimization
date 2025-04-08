import pytest
from hybrid_benchmark_suite import run_benchmark_suite

def dummy_algorithm(cfg):
    return cfg.get("value", 0)*2

def test_run_benchmark_suite():
    algs = {"dummy": dummy_algorithm}
    configs = [{"value":1}, {"value":2}]
    results = run_benchmark_suite(algs, configs)
    assert "dummy" in results
    assert len(results["dummy"]) == 2
