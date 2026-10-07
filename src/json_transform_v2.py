"""
JSON 转换脚本：把学生数据从旧格式转成新格式。

旧格式：
    {"id": "S001", "name": "张三", "score": "88"}

新格式：
    {"student_id": "S001", "student_name": "张三", "score": 88, "passed": true}
"""

import json
from typing import Optional
from pydantic import BaseModel, Field, ValidationError


class ClassInfo(BaseModel):
    """班级信息。"""
    name: str = Field(min_length=1, max_length=30)
    grade: int = Field(ge=1, le=12)


class StudentInput(BaseModel):
    """输入的学生数据模型。"""
    id: str = Field(pattern=r"^S\d{3}$", description="学号，格式 S + 3 位数字")
    name: str = Field(min_length=1, max_length=20, description="姓名")
    score: int = Field(ge=0, le=100, description="分数，0 到 100")
    class_info: Optional[ClassInfo] = Field(default=None, description="班级信息（可选）")


class StudentOutput(BaseModel):
    """输出的学生数据模型。"""
    student_id: str
    student_name: str
    score: int
    passed: bool
    class_name: Optional[str] = None


def transform_student(data: dict) -> dict:
    """
    把旧格式的学生数据转成新格式。

    Args:
        data: 旧格式字典，例如 {"id": "S001", "name": "张三", "score": "88"}

    Returns:
        新格式字典，例如 {"student_id": "S001", "student_name": "张三", "score": 88, "passed": true}

    Raises:
        ValidationError: 当数据不符合 StudentInput 模型时抛出。
    """
    student_in = StudentInput(**data)

    class_name: Optional[str] = None
    if student_in.class_info is not None:
        class_name = student_in.class_info.name

    student_out = StudentOutput(
        student_id=student_in.id,
        student_name=student_in.name,
        score=student_in.score,
        passed=student_in.score >= 60,
        class_name=class_name
    )

    return student_out.model_dump()


def safe_transform(data: dict) -> tuple[bool, Optional[dict], Optional[str]]:
    """
    安全转换：不抛异常，返回成功状态和数据。

    Args:
        data: 旧格式字典。

    Returns:
        (成功标志, 结果字典或 None, 错误信息或 None)
    """
    try:
        result = transform_student(data)
        return True, result, None
    except ValidationError as e:
        return False, None, str(e)


def main() -> None:
    """主函数：演示正常数据、字段缺失、非法值三种情况。"""
    good_data = {
        "id": "S001",
        "name": "张三",
        "score": "88",
        "class_info": {"name": "三年二班", "grade": 3}
    }
    ok, result, err = safe_transform(good_data)
    if ok:
        print("✅ 转换成功:", result)
        with open("data/student_output_v2.json", "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        print("已保存到 data/student_output_v2.json")

    missing_data = {"id": "S002", "score": "75"}
    ok, result, err = safe_transform(missing_data)
    if not ok:
        print("❌ 字段缺失:")
        print(err)

    bad_data = {"id": "X001", "name": "", "score": 150}
    ok, result, err = safe_transform(bad_data)
    if not ok:
        print("❌ 非法值:")
        print(err)


if __name__ == "__main__":
    main()