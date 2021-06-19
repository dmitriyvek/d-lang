from TokenType import TokenType


class Token:

    def __init__(self, type: TokenType, text: str, pos: int):
        self.type = type
        self.text = text
        self.pos = pos

    def __str__(self):
        return \
            f'<Token: type={self.type.name} text={self.text} pos={self.pos}>'
