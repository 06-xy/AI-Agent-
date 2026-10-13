"""test_api_to_json.py - api_to_json.py 的离线测试套件"""

import pytest
import requests

from api_to_json import fetch_repo


# ================= FakeResponse 类 =================

class FakeResponse:
    """模拟 requests.Response 对象"""

    def __init__(self, status_code: int, json_data: dict | None = None, error: str | None = None):
        self.status_code = status_code
        self._json_data = json_data
        self._error = error

    def json(self) -> dict:
        if self._error:
            raise requests.exceptions.HTTPError(self._error)
        return self._json_data if self._json_data else {}

    def raise_for_status(self) -> None:
        if self.status_code >= 400:
            raise requests.exceptions.HTTPError(
                f"HTTP {self.status_code}: {self._error}"
            )


# ================= 测试 1：200 成功 =================

def test_fetch_repo_success(monkeypatch):
    """测试 200 成功响应"""
    mock_resp = FakeResponse(
        status_code=200,
        json_data={
            "full_name": "python/cpython",
            "stargazers_count": 60000,
            "language": "Python"
        }
    )

    def fake_get(url, timeout):
        return mock_resp

    monkeypatch.setattr("requests.get", fake_get)

    result = fetch_repo("python/cpython")

    assert result is not None
    assert result["full_name"] == "python/cpython"
    assert result["stargazers_count"] == 60000


# ================= 测试 2：401 认证失败 =================

def test_fetch_repo_401(monkeypatch):
    """测试 401 未授权"""
    mock_resp = FakeResponse(
        status_code=401,
        error="Unauthorized: Invalid API key"
    )

    def fake_get(url, timeout):
        return mock_resp

    monkeypatch.setattr("requests.get", fake_get)

    result = fetch_repo("python/cpython")

    assert result is None


# ================= 测试 3：超时 =================

def test_fetch_repo_timeout(monkeypatch):
    """测试请求超时"""
    def fake_get(url, timeout):
        raise requests.Timeout("Read timed out")

    monkeypatch.setattr("requests.get", fake_get)

    result = fetch_repo("python/cpython")

    assert result is None


# ================= 测试 4：500 服务器错误 =================

def test_fetch_repo_500(monkeypatch):
    """测试 500 服务器错误"""
    mock_resp = FakeResponse(
        status_code=500,
        error="Internal Server Error"
    )

    def fake_get(url, timeout):
        return mock_resp

    monkeypatch.setattr("requests.get", fake_get)

    result = fetch_repo("python/cpython")

    assert result is None


# ================= 测试 5：网络连接失败 =================

def test_fetch_repo_connection_error(monkeypatch):
    """测试网络连接失败"""
    def fake_get(url, timeout):
        raise requests.ConnectionError("Network unreachable")

    monkeypatch.setattr("requests.get", fake_get)

    result = fetch_repo("python/cpython")

    assert result is None