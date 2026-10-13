"""pytest 全局配置：把 src/ 加入 Python 搜索路径。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))