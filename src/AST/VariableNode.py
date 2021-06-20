from ExpressionNode import ExpressionNode
from ..Token import Token


class VariableNode(ExpressionNode):

    def __init__(self, variable: Token):
        super().__init__()
        self.variable = variable
