import inspect

from docstring_parser import parse

# Python 类型到 JSON Schema 类型
_PY_TO_JSON = {
    "str": "string",
    "int": "integer",
    "float": "number",
    "bool": "boolean",
    "list": "array",
    "dict": "object",
}


def generate_tool_schema(func) -> dict:
    # 获取函数签名
    signature = inspect.signature(func)
    # 函数名
    name = func.__name__
    # raw docstring
    doc = inspect.getdoc(func) or ""
    parsed_doc = parse(doc)
    # 短描述
    description = parsed_doc.short_description
    # 参数
    params = parsed_doc.params
    properties = {}
    # 将参数转换成 openai tool schema 格式
    for param in params:
        properties[param.arg_name] = {
            "type": _PY_TO_JSON[param.type_name] if param.type_name else "null",
            "description": param.description,
        }
    # 根据函数签名中的参数默认值确定某个参数是否可选
    required = []
    for name, param in signature.parameters.items():
        # 如果默认参数是空，即没有默认参数，就说明是必须的
        if param.default is inspect.Parameter.empty:
            required.append(name)

    return {
        "type": "function",
        "function": {
            "name": name,
            "description": description,
            "parameters": {"type": "object", "properties": properties},
            "required": required,
        },
    }
