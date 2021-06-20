from typing import List

from errors import SyntaxError
from Token import Token
from TokenType import TokenType, token_type_dict


class Lexer:

    def __init__(self, code: str):
        self.pos = 0
        self.token_list: List[Token] = []
        self.code = code

    def lex_analysis(self) -> List[Token]:
        while (self.next_token()):
            pass

        def filter_func(token: Token):
            return token.type.name != token_type_dict['SPACE'].name

        self.token_list = list(filter(filter_func, self.token_list))
        return self.token_list

    def next_token(self) -> bool:
        if self.pos >= len(self.code):
            return False

        token_type_values: List[TokenType] = \
            list(token_type_dict.values())

        for i in range(len(token_type_values)):
            token_type = token_type_values[i]
            result = token_type.regex.match(self.code[self.pos:])

            if result and result.group(0):
                token = Token(
                    type=token_type,
                    text=result.group(0),
                    pos=self.pos
                )
                self.pos += len(result.group(0))
                self.token_list.append(token)
                return True

        raise SyntaxError(pos=self.pos)
