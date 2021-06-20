class SyntaxError(Exception):

    def __init__(self, pos: int):
        self.pos = pos

    def __str__(self):
        return f'There is an error on position {self.pos}'
