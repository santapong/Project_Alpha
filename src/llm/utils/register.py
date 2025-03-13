from typing import Callable

# Register Tool.
def register_tool(method: Callable):
    method.__is_tool = True
    return method

# Register Node.
def register_node(method: Callable):
    method.__is_node = True
    return method

# Register Edge.
def register_edge(method: Callable):
    method.__is_edge = True
    return method