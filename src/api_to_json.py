"""api_to_json.py - 从 GitHub API 获取仓库信息并保存 JSON"""

import json
import logging
from typing import Optional

import requests

# ================= 日志配置 =================
logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    encoding="utf-8"
)
logger = logging.getLogger(__name__)


def fetch_repo(repo: str, timeout: int = 10) -> Optional[dict]:
    """获取 GitHub 仓库信息。

    Args:
        repo: 仓库全名，如 "python/cpython"。
        timeout: 超时秒数。

    Returns:
        仓库信息字典，出错返回 None。
    """
    url = f"https://api.github.com/repos/{repo}"

    try:
        logger.info(f"开始请求 {repo}")
        resp = requests.get(url, timeout=timeout)
        resp.raise_for_status()
        data = resp.json()
        logger.info(f"{repo} 请求成功")
        return data
    except requests.Timeout:
        logger.error(f"{repo} 请求超时")
        return None
    except requests.ConnectionError:
        logger.error(f"{repo} 网络连接失败")
        return None
    except requests.HTTPError as e:
        logger.error(f"{repo} HTTP 错误: {e}")
        return None
    except KeyError as e:
        logger.error(f"{repo} 字段缺失: {e}")
        return None


def save_to_json(data: dict, filepath: str) -> None:
    """保存字典到 JSON 文件。"""
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def main() -> None:
    """主函数。"""
    repo = "python/cpython"
    data = fetch_repo(repo)

    if data is None:
        print("❌ 请求失败")
        return

    print(f"仓库: {data['full_name']}")
    print(f"Stars: {data['stargazers_count']}")
    print(f"Language: {data['language']}")

    save_to_json(data, "data/github_repo.json")
    print("已保存到 data/github_repo.json")


if __name__ == "__main__":
    main()