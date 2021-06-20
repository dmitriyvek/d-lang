from typing import Union, List

from errors import SyntaxError
from Token import Token
from TokenType import TokenType


class Parser:

    def __init__(self, token_list: List[Token]):
        self.pos = 0
        self.scope = {}
        self.token_list = token_list

    def match(self, expected: List[TokenType]) -> Union[Token, None]:
        if self.pos < len(self.token_list):
            current_token: Token = self.token_list[self.pos]

            def filter_func(elem: TokenType):
                return elem.name == current_token.type.name

            if (next(filter(filter_func, expected))):
                self.pos += 1
                return current_token

        return None

    def require(self, expected: List[TokenType]) -> Token:
        token = self.match(expected)
        if not token:
            raise SyntaxError(self.pos)

        return token
