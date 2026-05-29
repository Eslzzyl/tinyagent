from pathlib import Path


def read(path: Path | str) -> str:
    with open(path, mode="r", encoding="utf-8") as f:
        lines = f.readlines()
        return "\n".join(lines)


def write(path: Path | str, content: str) -> str:
    with open(path, mode="w", encoding="utf-8") as f:
        f.write(content)
    return f"Wrote file {path}"


tools = [
    {
        "type": "function",
        "function": {
            "name": "read",
            "description": "read a file from filesystem",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {
                        "type": "string",
                        "description": "file path",
                    },
                },
                "required": ["path"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "write",
            "description": "write a file to filesystem",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {
                        "type": "string",
                        "description": "file path",
                    },
                    "content": {
                        "type": "string",
                        "description": "content to write",
                    },
                },
                "required": ["content"],
            },
        },
    },
]
