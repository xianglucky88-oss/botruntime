import pytest

def test_dag_is_open_gap():
    from src.botruntime import dag
    with pytest.raises(NotImplementedError):
        dag.process({"id": "x"})

def test_recovery_is_open_gap():
    from src.botruntime import recovery
    with pytest.raises(NotImplementedError):
        recovery.process({"id": "x"})
