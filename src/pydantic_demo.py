from pydantic import BaseModel, ValidationError

class Student(BaseModel):
    name: str
    score: int

def main():
    data = {"name": "张三", "score": "88"}
    student = Student(**data)
    print(student)
    print(student.name)
    print(student.score)
    print(type(student.score))

    bad_data = {"name": "李四", "score": "abc"}
    try:
        Student(**bad_data)
    except ValidationError as e:
        print(f"校验失败: {e}")

if __name__ == "__main__":
    main()