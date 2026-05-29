from enum import Enum

from pydantic import BaseModel


class ToolCall(BaseModel):
    id: str
    name: str
    arguments: dict[str, str]


class Response(BaseModel):
    content: str
    tool_calls: list[ToolCall] | None


class Role(str, Enum):
    Assistant = "assistant"
    User = "user"
    System = "system"
    Tool = "tool"


class Message(BaseModel):
    role: Role
    content: str
    tool_call_id: str | None = None
