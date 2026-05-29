import os
from pathlib import Path


def read(path: str) -> str:
    """
    Read a file or folder from filesystem. If `path` is a folder, list all contents in it.

    Args:
        path (str) : the file or folder path
    """
    _path = Path(path)
    if _path.is_dir():
        return "\n".join(os.listdir(_path))
    else:
        with open(path, mode="r", encoding="utf-8") as f:
            lines = f.readlines()
            lines = [f"{index}:{lines[index]}" for index in range(1, len(lines))]

            return "".join(lines)


def write(path: str, content: str) -> str:
    """
    Write a file to filesystem.

    Args:
        path (str) : the file path
        content (str): the content to write
    """
    with open(path, mode="w", encoding="utf-8") as f:
        f.write(content)
    return f"Wrote file {path}"
