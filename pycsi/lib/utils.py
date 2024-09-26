import os

def path_to_module(root: str, path:str) -> str:
    """Return a normalized dotted path to a module relative to the root.

    Args:
        root (str): path to the root containing the module
        path (str): path to the module

    Returns:
        str: the dotted path to the module relative to the root
    """
    relative_path: str = os.path.relpath(path, root)
    relative_path = os.path.splitext(relative_path)[0]
    return relative_path.replace('/', '.')
