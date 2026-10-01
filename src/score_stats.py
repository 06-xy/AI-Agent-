import json


def get_max(scores: dict) -> int:
    """返回最高分。"""
    return max(scores.values())


def get_min(scores: dict) -> int:
    """返回最低分。"""
    return min(scores.values())


def get_avg(scores: dict) -> float:
    """返回平均分。"""
    return sum(scores.values()) / len(scores)


def get_fail_list(scores: dict) -> list:
    """返回不及格名单。"""
    return [name for name, score in scores.items() if score < 60]


def load_scores(filepath: str) -> dict:
    """从 JSON 文件读取分数。"""
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


def save_result(result: dict, filepath: str) -> None:
    """把统计结果保存到 JSON 文件。"""
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)


def main():
    scores = load_scores("data/scores.json")

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

    save_result(result, "data/score_result.json")
    print("已保存到 data/score_result.json")


if __name__ == "__main__":
    main()