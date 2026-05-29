from typing import Callable

from src.client import Client
from src.model import Message, Role
from src.tooling import tool
from src.tooling.parse import generate_tool_schema


class Agent:
    def __init__(self, client: Client, tools: list[Callable]):
        self.client = client
        self.tools = tools

    def run(self, request: str, max_iterations: int = 10):
        iteration = 1
        messages: list[Message] = []
        messages.append(Message(role=Role.User, content=request))
        while iteration < max_iterations:
            response = self.client.call_with_tools(
                messages=messages,
                tool_spec_list=[generate_tool_schema(tool) for tool in self.tools],
            )
            print(f"Assistant: {response.content}")
            messages.append(Message(role=Role.Assistant, content=response.content))
            if response.tool_calls:
                for call in response.tool_calls:
                    id = call.id
                    name = call.name
                    arguments = call.arguments
                    print(f"Tool: {name}({arguments})")
                    result = getattr(tool, name)(**arguments)
                    messages.append(
                        Message(role=Role.Tool, content=result, tool_call_id=id)
                    )
            else:
                break
