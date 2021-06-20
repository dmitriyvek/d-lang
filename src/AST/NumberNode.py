from ExpressionNode import ExpressionNode
from ..Token import Token


class NumberNode(ExpressionNode):

    def __init__(self, number: Token):
        super().__init__()
        self.number = number
