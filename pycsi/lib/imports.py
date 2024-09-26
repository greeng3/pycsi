"""Funtions for working with imports."""

import ast
import os
from typing import List
from dataclasses import dataclass
from .utils_ast import get_file_ast
from .utils import path_to_module

@dataclass
class Dependency:
    source: str
    imported: str
    alias: str
    
    
def extract_imports(root: str, path: str) -> List[Dependency]:
    """_summary_

    Args:
        root (str): path to the root of the files
        path (str): path to a file or directory with files

    Returns:
        List[Dependency]: list of import dependencies in the file or directory
    """
    imports: List[str] = []

    if os.path.isfile(path) and path.lower().endswith('.py'):
        imports += extract_imports_from_file(root, path)
    elif os.path.isdir(path):
        for subdir, _, files in os.walk(path):
            for file in files:
                if file.lower().endswith('.py'):
                    file_path: str = os.path.join(subdir, file)
                    imports += extract_imports_from_file(root, file_path)
          
    return imports


def extract_imports_from_file(root: str, path: str) -> List[Dependency]:
    """Extract the import dependencies from a single python file

    Args:
        root (str): the root of the files
        path (str): the path to a single python file

    Returns:
        List[Dependency]: a list of import dependencies
    """
    source: str = path_to_module(root, path)
    imports: List[Dependency] = []

    tree: ast.Module = get_file_ast(path)

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.append(Dependency(source, alias.name))
        elif isinstance(node, ast.ImportFrom):
            for alias in node.names:
                if node.level == 0:
                    imports.append(Dependency(source, alias.name))
                else:
                    prefix: str = source.rsplit('.', node.level)[0]
                    normalized: str = prefix + '.' + node.module
                    imports.append(Dependency(source, normalized, alias.name))

    return imports


# Usage example
# python_file_path = 'path/to/your/python/file.py'
# import_list = extract_imports(python_file_path)
# print(import_list)