import json

from openai import OpenAI
from openai.types.chat import ChatCompletionMessageFunctionToolCall

from src.model import Message, Response, ToolCall


def build_messages(messages: list[Message]) -> list:
    result = []
    for msg in messages:
        d = {"role": msg.role, "content": msg.content}
        if msg.tool_call_id:
            d["tool_call_id"] = msg.tool_call_id
        result.append(d)
    return result


class Client:
    def __init__(self, base_url: str, api_key: str, model):
        self.client = OpenAI(base_url=base_url, api_key=api_key)
        self.model = model

    def call_with_tools(
        self, messages: list[Message], tool_spec_list: list
    ) -> Response:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=build_messages(messages),
            tools=tool_spec_list,
            tool_choice="auto",
        )
        content = response.choices[0].message.content
        raw_tool_calls = response.choices[0].message.tool_calls
        tool_call_list: list[ToolCall] = []
        if raw_tool_calls:
            for call in raw_tool_calls:
                assert type(call) is ChatCompletionMessageFunctionToolCall
                raw_arguments = call.function.arguments
                arguments = json.loads(raw_arguments)
                tool_call = ToolCall(
                    id=call.id,
                    name=call.function.name,
                    arguments=arguments,
                )
                tool_call_list.append(tool_call)

        return Response(content=content if content else "", tool_calls=tool_call_list)
