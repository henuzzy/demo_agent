from importlib.metadata import metadata

from pydantic import basemodel
from typing import Literal, Dict, Any
from datetime import datetime


MessageRole = Literal["user", "assitant", "system", "tool"]

class Message(basemodel):
    """消息类"""

    content: str
    role: MessageRole
    timestamp: datetime = None

    # Python3.9 + → 用dict[str, Any]。
    # Python3.8及以下 → 用Dict[str, Any]。
    metadata: Dict[str, Any] | None = None

    def __init__(self, content: str, role: MessageRole, **kwargs):
        super().__init__(
            content = content,
            role = role,
            timestamp = kwargs.get("timestamp", datetime.now()),
            metadata = kwargs.get("metadata", {})
        )

    def to_dict(self) -> Dict[str, Any]:
        """转换为字典格式（OpenAI API格式）"""
        return {
            "role": self.role,
            "content": self.content
        }

    def __str__(self) -> str:
        return f"[{self.role}] {self.content}"


