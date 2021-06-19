import re


class TokenType:

    def __init__(self, name: str, regex: re.Pattern):
        self.name = name
        self.regex = regex

    def __str__(self):
        return f'<TokenType: name={self.name} regex={self.regex}>'


# TODO: dataclass
token_type_dict = {
    'NUMBER': TokenType(name='NUMBER', regex=re.compile('[0-9]*')),
    'VARIABLE': TokenType(name='VARIABLE', regex=re.compile('[а-я]*')),
    'SEMICOLON': TokenType(name='SEMICOLON', regex=re.compile(';')),
    'SPACE': TokenType(name='SPACE', regex=re.compile('[ \\n\\t\\r]')),
    'ASSIGN': TokenType(name='ASSIGN', regex=re.compile('РАВНО')),
    'CONSOLE': TokenType(name='CONSOLE', regex=re.compile('КОНСОЛЬ')),
    'PLUS': TokenType(name='PLUS', regex=re.compile('ПЛЮС')),
    'MINUS': TokenType(name='MINUS', regex=re.compile('МИНУС')),
    'LPAR': TokenType(name='LPAR', regex=re.compile('\\(')),
    'RPAR': TokenType(name='RPAR', regex=re.compile('\\)')),
}
