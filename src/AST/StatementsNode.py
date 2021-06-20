from typing import List

from ExpressionNode import ExpressionNode


class StatementsNode(ExpressionNode):

    def __init__(self):
        super().__init__()
        self.code_strings: List[ExpressionNode] = []

    def add_node(self, node: ExpressionNode):
        self.code_strings.append(node)
