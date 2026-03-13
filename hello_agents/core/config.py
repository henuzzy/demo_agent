"""配置管理"""
import os
from optparse import IndentedHelpFormatter
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
    # tool_output_max_lines: int = 2000   # 工具输出最大行数
    # tool_output_max_bytes: int = 512000 #工具输出最大字节数（50KB）
    # tool_output_truncate_direction: str = "head" # 截断方向：head/tail/head_tail
    # tool_output_output_dir: str = "tool_output" # 完整输出保存目录

    # 系统配置
    debug: bool = False
    log_level: str = "INFO"

    # 其他配置
    max_history_length: int = 100

    @classmethod
    def from_env(cls) -> "Config":
        """从环境变量创建配置"""
        return cls(
            debug = os.getenv("DEBUG", "false").lower == "true",
            log_level = os.getenv("LOG_LEVEL", "INFO"),
            temperature = float(os.getenv("TEMPERATURE", 0.7)),
            max_tokens = int(os.getenv("MAX_TOKENS")) if os.getenv("MAX_TOKENS") else None,
        )

    def to_tict(self) -> Dict[str, Any]:
        """把对象转换成字典形式"""
        return self.dict()

