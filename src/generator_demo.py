"""手写生成器，理解 yield 的原理。"""
from typing import Generator


def number_stream(n: int) -> Generator[int, None, None]:
    """
    生成 0 到 n-1 的数字流。

    Args:
        n: 生成多少个数字。

    Yields:
        每次产出一个整数。
    """
    for i in range(n):
        print(f"[number_stream] 准备产出 {i}")
        yield i


def chunk_stream(text: str) -> Generator[str, None, None]:
    """
    把文本切成一个个字符，模拟流式输出。

    Args:
        text: 输入文本。

    Yields:
        每次产出一个字符。
    """
    for ch in text:
        yield ch


def main() -> None:
    """演示生成器。"""
    print("=== 示例 1：数字流 ===")
    for num in number_stream(3):
        print(f"收到 {num}")

    print("\n=== 示例 2：字符流 ===")
    for ch in chunk_stream("你好世界"):
        print(f"收到: {ch}", end=" ")
    print()


if __name__ == "__main__":
    main()