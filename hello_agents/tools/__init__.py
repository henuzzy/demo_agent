"""工具系统"""

from hello_agents.tools.base import Tool, ToolParameter
from hello_agents.tools.registry import ToolRegistry, global_registry

# 内置工具


# 协议工具


# 高级功能
from hello_agents.tools.chain import ToolChain, ToolChainManager, create_research_chain, create_simple_chain


__all__ = [
    # 基础工具系统
    "Tool",
    "ToolParameter",
    "ToolRegistry",
    "global_registry",

    # 内置工具


    # 协议工具



    # 工具链功能

]