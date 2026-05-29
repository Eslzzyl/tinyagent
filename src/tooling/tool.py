def read(path: str) -> str:
    """
    read a file from filesystem.

    Args:
        path (str) : the file path
    """
    with open(path, mode="r", encoding="utf-8") as f:
        lines = f.readlines()
        return "\n".join(lines)


def write(path: str, content: str) -> str:
    """
    write a file to filesystem.

    Args:
        path (str) : the file path
        content (str): the content to write
    """
    with open(path, mode="w", encoding="utf-8") as f:
        f.write(content)
    return f"Wrote file {path}"
