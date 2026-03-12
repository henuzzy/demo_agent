"""配置管理"""
import os
from typing import Dict, Any
from pydantic import baseModel

class Config(baseModel):
    """hello agents 配置类管理"""

    # llm配置
    default_model: str = "gpt-3.5-turbo"
    default_provide: str = "openai"
    temperature: float = 0.7
    max_tokens: int | None = None

    # 工具输出截断配置
    tool_output_max_lines: int = 2000   # 工具输出最大行数
    tool_output_max_bytes: int = 512000 #工具输出最大字节数（50KB）
    tool_output_truncate_direction: str = "head" # 截断方向：head/tail/head_tail
    tool_output_output_dir: str = "tool_output" # 完整输出保存目录
