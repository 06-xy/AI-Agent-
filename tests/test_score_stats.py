"""test_score_stats.py - score_stats.py 的测试套件"""

import pytest

from score_stats import get_max, get_min, get_avg, get_fail_list


# ================= 正常情况 =================

def test_get_max_normal():
    scores = {"张三": 88, "李四": 55, "王五": 92}
    assert get_max(scores) == 92


def test_get_min_normal():
    scores = {"张三": 88, "李四": 55, "王五": 92}
    assert get_min(scores) == 55


def test_get_avg_normal():
    scores = {"张三": 80, "李四": 60, "王五": 100}
    assert get_avg(scores) == 80.0


def test_get_fail_list_normal():
    scores = {"张三": 88, "李四": 55, "王五": 47}
    result = get_fail_list(scores)
    assert "李四" in result
    assert "王五" in result
    assert "张三" not in result


# ================= 边界情况 =================

def test_get_max_single():
    scores = {"张三": 100}
    assert get_max(scores) == 100


def test_get_fail_list_empty():
    scores = {"张三": 88, "李四": 92}
    assert get_fail_list(scores) == []


# ================= 异常情况 =================

def test_get_max_empty():
    with pytest.raises(ValueError):
        get_max({})


def test_get_avg_empty():
    with pytest.raises(ZeroDivisionError):
        get_avg({})