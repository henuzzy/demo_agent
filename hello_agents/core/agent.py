from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional
import asyncio
from hello_agents.core.config import Config


class Agent(ABC):
    """
    agent基类
    集成能力：
    - HistoryManager：历史管理与压缩
    - ObservationTruncator：工具截断于输出
    - TraceLogger: 可观测性（JSONL + HTML）
    - ToolRegistry: 工具管理（可选）
    - SkillLoader: 知识外化（可选）
    """

    def __init__(
        self,
        name: str,
        llm: HelloAgentsLLM,
        # system_prompt: Optional[str] = None,
        system_prompt: str | None = None,
        config: Optional[Config] = None,
        # tool_registry: ToolRegistry | None = None,
    ):
        self.name = name
        self.llm = llm
        self.system_prompt = system_prompt
        self.config = config or Config()
        self.history: list[Message] = []

        @abstractmethod
        def run(self, input_text: str, **kwargs) -> str:
            """运行agent"""
            pass

        def add_message(self, message: Message):
            """添加消息到历史记录"""
            self.history.append(message)

        def clear_history(self):
            """清空历史记录"""
            self.histoy.clear()

        def __str__(self) -> str:
            return f"Agent(name={self.name}, provider={self.llm.provider})"

        def __repr__(self) -> str:
            return self.__str__()



        # 工具注册表（可选）
        # self.tool_registry = tool_registry

        # 新增：上下文工程组件
        # from hello_agents.context.history import HistoryManager
        # from hello_agents.context.truncator import ObservationTruncator
        #
        # self.history_manager = HistoryManager(
        #     min_retain_rounds = self.config.min_retain_rounds,
        #     compression_threshold = self.config.compression_threshold
        # )
        #
        # self.truncator = ObservationTruncator(
        #     max_lines = self.config.tool_output_max_lines,
        #     max_bytes = self.config.tool_output_max_bytes,
        #     truncate_direction = self.config.tool_output_truncate_direction,
        #     output_dir = self.config.tool_output_dir
        # )
