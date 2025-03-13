from typing import Callable
from langgraph.graph import START, END, StateGraph
 
 
 

# Decorator that will automatic create workflow.
# NOTE: Make it can create Condition.
def workflow(func: Callable):
    def create_workflow(start_key, end_key, group_name, node_name, **args):
        return
    return


#TODO: I think does it need to create STATEGRAPH here.