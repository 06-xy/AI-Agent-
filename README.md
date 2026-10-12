# AI-Agent 学习项目

2028 届民办二本计科，深圳求职，AI Agent 学习路线。

## 项目结构

```text
AI-Agent学习/
├── src/                  # 源代码
│   ├── score_stats.py    # 成绩统计
│   ├── utils.py          # 工具函数
│   └── pydantic_demo.py  # Pydantic 示例
├── tests/                # 测试
│   └── test_score_stats.py
├── data/                 # 数据
├── logs/                 # 日志
├── docs/                 # 文档
├── job-requirements.md
├── job-tracker.md
├── budget.md
├── progress.md
├── direction-check.md
└── interview-qa.md



# ========== 代码质量检查 ==========

# 1. 安装依赖
pip install -r requirements.txt

# 2. 运行测试 + 覆盖率（要求 Cover ≥ 80%）
pytest --cov=src --cov-report=term-missing tests/ -v

# 3. 代码规范检查（要求 All checks passed）
ruff check src/
# 自动修复：
ruff check --fix src/
ruff check --fix --unsafe-fixes src/

# 4. 类型检查（要求 Success: no issues found）
mypy src/

# ========== 一键运行全部 ==========
pytest --cov=src --cov-report=term-missing tests/ -v && \
ruff check src/ && \
mypy src/