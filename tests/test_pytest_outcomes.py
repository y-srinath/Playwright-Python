import pytest

@pytest.mark.demo
def test_fail_assert():
    assert 12 * 12 == 143

@pytest.mark.demo
@pytest.mark.xfail
def test_xfail():
    assert False
    
@pytest.mark.demo
@pytest.mark.xfail
def test_xpass():
    assert True