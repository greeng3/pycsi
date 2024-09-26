from functools import cache
import ast

@cache
def get_file_ast(path: str) -> ast.Module:
    """Read in a python file and return the module ast for it.  Also, cache it, in the event it is requested more than
       once.

    Args:
        path (str): the path to a python file

    Returns:
        ast.Module: the ast for the module expressed by that file
    """
    with open(path) as f_in:
        tree: ast.Module = ast.parse(f_in.read())
        
    return tree
