import textwrap

from Lexer import Lexer

code = textwrap.dedent('''\
    код РАВНО 5 ПЛЮС 9 ПЛЮС ( 4 МИНУС 6 );
    КОНСОЛЬ код;
    переменная РАВНО код ПЛЮС 3;
    КОНСОЛЬ переменная ПЛЮС код МИНУС 6;
''')

code2 = 'код РАВНО 5 ПЛЮС 9 ПЛЮС ( 4 МИНУС 6 );'

lexer = Lexer(code=code)
lexer.lex_analysis()

print(list(map(lambda x: str(x), lexer.token_list)))
