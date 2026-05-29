import os
from pathlib import Path


def read(path: str, offset: int | None = None, limit: int | None = None) -> str:
    """
    Read a file or folder from filesystem. If `path` is a folder, list all contents in it.

    Args:
        path (str): The file or folder path
        offset (int, optional): The starting line number to read (starting from 1).
        limit (int, optional): Number of lines to read
    """
    _path = Path(path)
    if _path.is_dir():
        return "\n".join(os.listdir(_path))
    else:
        if offset and offset < 1:
            return f"Error: invalid offset: {offset}"
        if limit and limit < 1:
            return f"Error: invalid limit: {limit}"

        with open(path, mode="r", encoding="utf-8") as f:
            lines = f.readlines()
            lines = [f"{index}:{lines[index]}" for index in range(1, len(lines))]
            if not offset:
                offset = 1
            if offset - 1 > len(lines):
                return f"Error: offset {offset} is larger than file line counts {len(lines)}"
            # 截取从 offset 开始的所有行
            lines = lines[offset - 1 :]
            if limit:
                if limit > len(lines):
                    return f"Error: limit {offset} is larger than file line counts {len(lines)} from offset {offset}"
                lines = lines[:limit]

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
