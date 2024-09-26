from typing import Set
import os
import tomlkit
import pkgutil

NATIVE_MODULES: Set[str] = {item.name for item in pkgutil.iter_modules()}

POETRY_LOCK_NAME: str = 'poetry.lock'

def get_poetry_modules(root: str) -> Set[str]:
    """Get all the packages in the poetry.lock file

    Args:
        root (str): the path of the directory containing the poetry.lock file

    Returns:
        Set[str]: the names of all the packages installed in the poetry.lock file
    """
    poetry_modules: Set[str] = set()
    
    poetry_lock_path: str = os.path.join(root, POETRY_LOCK_NAME)
    if not os.path.isfile(poetry_lock_path):
        # no lock file -> no poetry modules
        return poetry_modules
    
    with open(poetry_lock_path, 'r') as f_in:
        data = tomlkit.parse(f_in.read())
        for package in data['package']:
            poetry_modules.add(package['name'])
    return poetry_modules
