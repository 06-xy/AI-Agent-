"""手写上下文管理器，理解 with 的原理。"""


class MyFile:
    """模拟文件类，支持 with 语句。"""

    def __init__(self, filename: str, mode: str) -> None:
        """初始化时保存文件名和模式，不打开文件。"""
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        """进入 with 时调用，打开文件并返回。"""
        print(f"[MyFile] 打开文件 {self.filename}")
        self.file = open(self.filename, self.mode, encoding="utf-8")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        """退出 with 时调用，关闭文件。"""
        print(f"[MyFile] 关闭文件 {self.filename}")
        if self.file is not None:
            self.file.close()
        return False


def main() -> None:
    """演示用 with 管理资源。"""
    with MyFile("data/test.txt", "w") as f:
        f.write("hello\n")
        f.write("world\n")

    with MyFile("data/test.txt", "r") as f:
        content = f.read()
        print("文件内容:")
        print(content)


if __name__ == "__main__":
    main()