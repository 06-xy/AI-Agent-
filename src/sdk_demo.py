"""模拟 LLM SDK 的资源管理和流式输出。"""
from typing import Generator


class MockLLMClient:
    """模拟 LLM 客户端，支持 with 和流式输出。"""

    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
        self.connected = False

    def __enter__(self):
        """进入 with 时连接。"""
        print("[MockLLMClient] 连接服务器...")
        self.connected = True
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """退出 with 时断开。"""
        print("[MockLLMClient] 断开连接")
        self.connected = False
        return False

    def chat_stream(self, prompt: str) -> Generator[str, None, None]:
        """模拟流式聊天，逐字返回。"""
        if not self.connected:
            raise RuntimeError("客户端未连接")
        response = f"你说的是：{prompt}"
        for ch in response:
            yield ch


def main() -> None:
    """演示 SDK 用法。"""
    with MockLLMClient(api_key="fake-key") as client:
        print("用户: 你好")
        print("AI: ", end="")
        for chunk in client.chat_stream("你好"):
            print(chunk, end="", flush=True)
        print()


if __name__ == "__main__":
    main()