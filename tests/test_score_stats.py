from score_stats import get_max, get_min, get_avg, get_fail_list

def test_get_max():
    scores = {"a": 88, "b": 55, "c": 92}
    assert get_max(scores) == 92

def test_get_min():
    scores = {"a": 88, "b": 55, "c": 92}
    assert get_min(scores) == 55

def test_get_avg():
    scores = {"a": 80, "b": 60, "c": 100}
    assert get_avg(scores) == 80.0

def test_get_fail_list():
    scores = {"a": 88, "b": 55, "c": 47}
    result = get_fail_list(scores)
    assert "b" in result
    assert "c" in result
    assert "a" not in result