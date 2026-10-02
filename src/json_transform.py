import json
from pydantic import BaseModel, Field, ValidationError

class StudentInput(BaseModel):
    id: str = Field(pattern=r"S\d{3}$")
    name: str = Field(min_length=1, max_length=20)
    score: int = Field(ge=0, le=100)

class StudentOutput(BaseModel):
    student_id: str
    student_name: str
    score: int
    passed: bool

def transform_student(data: dict) -> dict:
    student_in = StudentInput(**data)
    student_out = StudentOutput(
        student_id=student_in.id,
        student_name=student_in.name,
        score=student_in.score,
        passed=student_in.score >= 60
    )
    return student_out.model_dump()

def main():
    good_data = {"id": "S001", "name": "张三", "score": 88}
    result = transform_student(good_data)
    print("转换成功：", result)

    with open("data/student_output.json", "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print("已保存到 data/student_output.json")

    bad_data = {"id": "x001", "name": "", "score": 150}
    try:
        transform_student(bad_data)
    except ValidationError as e:
        print(f"❌ 校验失败：{e}")

if __name__ == "__main__":
    main()