from ExpressionNode import ExpressionNode
from ..Token import Token


class UnarOperationNode(ExpressionNode):

    def __init__(self, operator: Token, operand: ExpressionNode):
        super().__init__()
        self.operator = operator
        self.operand = operand
