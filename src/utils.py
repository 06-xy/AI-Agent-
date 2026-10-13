"""
utils.py —— 项目公共工具函数

职责：JSON 读写 + 日志配置 + 常量配置。
不包含任何业务逻辑（不算分、不调 API、不做转换）。
"""

# ---------- 1. 标准库导入 ----------
import json
import logging
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

# ---------- 2. 类型别名：让签名可读 ----------
JsonDict = dict[str, Any]      # 用 Any 是因为 JSON 的值类型不固定
JsonList = list[dict[str, Any]]

# ---------- 3. 自定义异常：比裸抛 ValueError 更明确 ----------
class DataError(Exception):
    """数据读取/校验失败时抛出。

    好处：调用方可以专门 except DataError，
    而不会误捕获别的 ValueError（比如 int("abc") 那种）。
    """
    pass


# ---------- 4. 配置对象：消灭魔法字符串 ----------
@dataclass(frozen=True)
class AppConfig:
    """应用配置。frozen=True 表示创建后不可修改，防止被意外改掉。"""
    input_path: Path = Path("data/input.json")
    output_path: Path = Path("data/output.json")
    encoding: str = "utf-8"
    indent: int = 2
    # field(default_factory=...) 用于可变默认值，今天用不上但记住这个坑：
    # ❌ tags: list[str] = []   ← 所有实例会共享同一个 list！
    # ✅ tags: list[str] = field(default_factory=list)


# ---------- 5. 读 JSON ----------
def read_json(path: str | Path, encoding: str = "utf-8") -> JsonDict:
    """读取 JSON 文件，返回字典。

    Args:
        path: 文件路径（字符串或 Path 都行）
        encoding: 编码，默认 utf-8

    Returns:
        解析后的字典

    Raises:
        FileNotFoundError: 文件不存在
        DataError: JSON 格式错误或解析结果不是字典
    """
    p = Path(path)                      # 统一转成 Path，后面好用
    if not p.exists():
        raise FileNotFoundError(f"数据文件不存在: {p.absolute()}")

    try:
        with p.open("r", encoding=encoding) as f:   # Path.open 等价于 open()
            data = json.load(f)
    except json.JSONDecodeError as e:
        # ★ 重点：把底层异常包装成我们的 DataError，并保留原始信息
        raise DataError(f"JSON 格式错误: {e}") from e

    if not isinstance(data, dict):
        raise DataError(f"JSON 根节点必须是对象(dict)，实际是 {type(data).__name__}")

    return data


# ---------- 6. 写 JSON ----------
def write_json(
    data: Any,
    path: str | Path,
    encoding: str = "utf-8",
    indent: int = 2,
) -> Path:
    """把数据写成 JSON 文件。

    Returns:
        写入成功的文件路径（方便链式调用和断言）
    """
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)     # ★ 自动创建上级目录，超实用

    with p.open("w", encoding=encoding) as f:
        json.dump(data, f, ensure_ascii=False, indent=indent)

    return p


# ---------- 7. 日志配置 ----------
def setup_logger(name: str = "app", level: int = logging.DEBUG) -> logging.Logger:
    """获取或创建一个配置好的 logger。

    注意：logging.getLogger(name) 同一个 name 多次调用返回同一个对象，
    所以要避免重复添加 handler（否则一条日志打印两遍）。
    """
    logger = logging.getLogger(name)
    if logger.handlers:               # 已经配置过就直接返回
        logger.setLevel(level)
        return logger

    logger.setLevel(level)
    handler = logging.StreamHandler()
    fmt = "%(asctime)s %(levelname)-8s %(name)s:%(lineno)d %(message)s"
    handler.setFormatter(logging.Formatter(fmt))
    logger.addHandler(handler)
    return logger