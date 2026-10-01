import json

def save_json(data, filepath: str) -> None:
    """保存数据到 JSON 文件。"""
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def load_json(filepath: str) -> dict:
    """从 JSON 文件读取数据。"""
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)