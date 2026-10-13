"""json_transform.py - JSON 数据转换脚本

读取原始 JSON 数据，通过 Pydantic 验证，转换为标准化输出。
"""

import json
import logging
from typing import List, Optional

from pydantic import BaseModel, Field, ValidationError

# ================= 日志配置 =================
logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    encoding="utf-8"
)
logger = logging.getLogger(__name__)


# ================= 输入模型 =================
class StudentInput(BaseModel):
    """学生成绩输入模型。"""
    name: str = Field(..., min_length=1, max_length=20)
    age: int = Field(..., ge=0, le=150)
    scores: List[int] = Field(..., min_length=1)

    def average(self) -> float:
        """计算平均分。"""
        return sum(self.scores) / len(self.scores)

    def grade(self) -> str:
        """根据平均分判定等级。"""
        avg = self.average()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        return "F"


# ================= 输出模型 =================
class StudentOutput(BaseModel):
    """学生成绩输出模型。"""
    name: str
    avg_score: float
    grade: str


def transform_student(student_data: dict) -> StudentOutput:
    """把原始字典转换为标准化输出。

    Args:
        student_data: 原始学生数据字典。

    Returns:
        StudentOutput 实例。

    Raises:
        ValidationError: 数据不合法时抛出。
    """
    student = StudentInput(**student_data)
    return StudentOutput(
        name=student.name,
        avg_score=round(student.average(), 2),
        grade=student.grade()
    )


def transform_json_file(input_path: str, output_path: str) -> int:
    """读取 JSON 文件，批量转换并写入新文件。

    Args:
        input_path: 输入 JSON 路径。
        output_path: 输出 JSON 路径。

    Returns:
        成功转换的记录数。
    """
    with open(input_path, "r", encoding="utf-8") as f:
        students = json.load(f)

    results = []
    for student_data in students:
        result = transform_student(student_data)
        results.append(result.model_dump())

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    logger.info(f"转换了 {len(results)} 条记录")
    return len(results)


def main() -> None:
    """主函数。"""
    try:
        count = transform_json_file(
            "data/students.json",
            "data/student_output.json"
        )
        print(f"✅ 成功转换 {count} 条记录")
    except FileNotFoundError as e:
        print(f"❌ 文件不存在: {e}")
    except ValidationError as e:
        print(f"❌ 数据校验失败: {e}")


if __name__ == "__main__":
    main()