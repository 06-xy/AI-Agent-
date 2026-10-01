from utils import save_json

def get_max(scores: dict) -> int:
    return max(scores.values())

def get_min(scores: dict) -> int:
    return min(scores.values())

def get_avg(scores: dict) -> float:
    return sum(scores.values()) / len(scores)

def get_fail_list(scores: dict) -> list:
    return [name for name, score in scores.items() if score < 60]

def main():
    scores = {
        "张三": 88,
        "李四": 55,
        "王五": 92,
        "赵六": 47,
        "钱七": 73,
    }

    result = {
        "max": get_max(scores),
        "min": get_min(scores),
        "avg": get_avg(scores),
        "fail_list": get_fail_list(scores),
    }

    print(f"最高分: {result['max']}")
    print(f"最低分: {result['min']}")
    print(f"平均分: {result['avg']:.1f}")
    print(f"不及格名单: {result['fail_list']}")

    save_json(result, "data/score_result.json")
    print("已保存到 data/score_result.json")

if __name__ == "__main__":
    main()