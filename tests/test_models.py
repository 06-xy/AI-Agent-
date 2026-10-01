import pytest
from pydantic import ValidationError
from models import Student

def test_valid():
    s = Student(name="张三", score=88)
    assert s.score == 88

def test_auto_convert():
    s = Student(name="张三", score="88")
    assert isinstance(s.score, int)

def test_invalid_score():
    with pytest.raises(ValidationError):
        Student(name="张三", score=150)

def test_missing_name():
    with pytest.raises(ValidationError):
        Student(score=88)