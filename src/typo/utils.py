# src/typo/utils.py

def remove_comments(code: str) -> str:
    """
    Remove comments from Python code.

    Parameters:
    code (str): The original Python code.

    Returns:
    str: The code without comments.
    """
    import re
    return re.sub(r'#.*', '', code)

def remove_docstrings(code: str) -> str:
    """
    Remove docstrings from Python code.

    Parameters:
    code (str): The original Python code.

    Returns:
    str: The code without docstrings.
    """
    import ast

    class DocstringRemover(ast.NodeTransformer):
        def visit_FunctionDef(self, node):
            node.body = [n for n in node.body if not isinstance(n, ast.Expr) or not isinstance(n.value, ast.Str)]
            self.generic_visit(node)
            return node

    tree = ast.parse(code)
    DocstringRemover().visit(tree)
    return ast.unparse(tree)

def extract_function_names(code: str) -> list:
    """
    Extract function names from Python code.

    Parameters:
    code (str): The original Python code.

    Returns:
    list: A list of function names.
    """
    import ast

    class FunctionNameExtractor(ast.NodeVisitor):
        def __init__(self):
            self.function_names = []

        def visit_FunctionDef(self, node):
            self.function_names.append(node.name)
            self.generic_visit(node)

    tree = ast.parse(code)
    extractor = FunctionNameExtractor()
    extractor.visit(tree)
    return extractor.function_names

def validate_syntax(code: str) -> bool:
    """
    Validate the syntax of Python code.

    Parameters:
    code (str): The original Python code.

    Returns:
    bool: True if syntax is valid, False otherwise.
    """
    import ast

    try:
        ast.parse(code)
        return True
    except SyntaxError:
        return False
