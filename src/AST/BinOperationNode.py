from ExpressionNode import ExpressionNode
from ..Token import Token


class BinOperationNode(ExpressionNode):

    def __init__(
        self,
        operator: Token,
        leftNode: ExpressionNode,
        rightNode: ExpressionNode
    ):
        super().__init__()
        self.operator = operator
        self.leftNode = leftNode
        self.rightNode = rightNode
