# AI-Agent 学习项目

Python 工程化练习项目。包含三个脚本：成绩统计、JSON 数据转换、GitHub API 数据获取。

## 项目背景

学习 AI Agent 开发过程中的阶段 A 练习项目。目标是从"会写代码"过渡到"工程化开发"，掌握：

- 类型标注（Type Hints）
- Pydantic 数据校验
- pytest 自动化测试
- monkeypatch Mock 测试
- 代码覆盖率与代码质量工具
- Git 版本控制

## 项目结构

```text
AI-Agent学习/
├── src/
│   ├── api_to_json.py        # GitHub API 数据获取并保存 JSON
│   ├── score_stats.py        # 学生成绩统计
│   └── json_transform.py     # JSON 数据转换与 Pydantic 校验
├── tests/
│   ├── test_api_to_json.py
│   ├── test_score_stats.py
│   └── test_models.py
├── data/                     # 数据输出
├── logs/                     # 日志文件
├── docs/                     # 学习笔记
├── README.md
├── .env.example
├── .gitignore
└── requirements.txt
```

## 环境要求

- Python 3.12+
- pip
- Git

## 安装

```bash
# 克隆仓库
git clone https://github.com/06-xy/AI-Agent学习.git
cd AI-Agent学习

# 创建虚拟环境
python3 -m venv venv
source venv/bin/activate      # Linux / macOS
# venv\Scripts\activate       # Windows

# 安装依赖
pip install -r requirements.txt
```

## 环境变量

复制 `.env.example` 为 `.env`，填入真实值：

```bash
cp .env.example .env
```

`.env` 内容示例：

```text
API_KEY=your_api_key_here
BASE_URL=https://api.deepseek.com
MODEL=deepseek-chat
LOG_LEVEL=INFO
```

> `.env` 已在 `.gitignore` 中，不会被提交到仓库。

## 运行

### 1. 成绩统计

```bash
python src/score_stats.py
```

功能：读取学生成绩数据，计算最高分、最低分、平均分和不及格名单。

### 2. JSON 数据转换

```bash
python src/json_transform.py
```

功能：读取原始 JSON 数据，通过 Pydantic 模型验证，转换为标准化输出。

### 3. API 数据获取

```bash
python src/api_to_json.py
```

功能：调用 GitHub API 获取仓库信息，保存为 JSON 文件到 `data/` 目录。

> 需要联网。若在国内网络不稳定，可使用 Mock 测试替代（见测试章节）。

## 测试

### 运行所有测试

```bash
pytest tests/ -v
```

### 运行单个测试文件

```bash
pytest tests/test_api_to_json.py -v
```

### 覆盖率报告

```bash
pytest --cov=src --cov-report=term-missing tests/ -v
```

### 生成 HTML 覆盖率报告

```bash
pytest --cov=src --cov-report=html tests/
# 打开 htmlcov/index.html 查看
```

## 代码质量检查

```bash
# 代码规范
ruff check src/

# 自动修复
ruff check --fix src/

# 类型检查
mypy src/
```

## 技术栈

| 能力 | 工具 |
|---|---|
| HTTP 请求 | requests |
| 数据校验 | Pydantic v2 |
| 测试框架 | pytest |
| Mock 测试 | monkeypatch |
| 覆盖率 | pytest-cov |
| 代码规范 | ruff |
| 类型检查 | mypy |
| 版本控制 | Git + GitHub |

## 已知局限

- API 脚本目前只支持 GitHub 仓库信息，未做通用化封装
- 未实现请求重试机制
- 覆盖率报告需本地生成，未接入 CI

## 后续计划

- 进入阶段 B：LLM API 调用、FastAPI 服务化、工具调用
- 增加更多异常场景测试
- 接入 GitHub Actions 最小 CI

## 许可

MIT License