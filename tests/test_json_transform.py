"""test_json_transform.py - json_transform.py 的测试套件"""

import pytest
from pydantic import ValidationError

from json_transform import StudentInput, StudentOutput, transform_student


# ================= StudentInput 校验 =================

def test_student_valid():
    s = StudentInput(name="张三", age=20, scores=[90, 85, 92])
    assert s.name == "张三"
    assert s.age == 20
    assert s.scores == [90, 85, 92]


def test_student_auto_convert():
    s = StudentInput(name="张三", age="20", scores=[90])
    assert isinstance(s.age, int)
    assert s.age == 20


def test_student_invalid_age():
    with pytest.raises(ValidationError):
        StudentInput(name="张三", age=200, scores=[90])


def test_student_empty_scores():
    with pytest.raises(ValidationError):
        StudentInput(name="张三", age=20, scores=[])


def test_student_missing_name():
    with pytest.raises(ValidationError):
        StudentInput(age=20, scores=[90])


# ================= 等级计算 =================

def test_grade_a():
    s = StudentInput(name="张三", age=20, scores=[95, 92])
    assert s.grade() == "A"


def test_grade_d():
    s = StudentInput(name="张三", age=20, scores=[55, 60])
    assert s.grade() == "D"


# ================= transform_student =================

def test_transform_success():
    data = {"name": "张三", "age": 20, "scores": [90, 85, 92]}
    result = transform_student(data)
    assert isinstance(result, StudentOutput)
    assert result.name == "张三"
    assert result.grade == "A"
    assert result.avg_score == 89.0