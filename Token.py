

class Token:

    def __init__(self, row_number, column_number, lexeme, tok_type):

        if row_number <= 0:
            raise Exception("IllegalArgumentException, invalid row number argument")
        if column_number <= 0:
            raise Exception("IllegalArgumentException, invalid column number argument")
        if lexeme is None or 0 == len(lexeme):
            raise Exception("IllegalArgumentException, invalid lexeme argument")
        if tok_type is None:
            raise Exception("IllegalArgumentException, invalid TokenType argument")
        self.row_number = row_number
        self.column_number = column_number
        self.lexeme = lexeme
        self.tok_type = tok_type

    def get_row_number(self):
        return self.row_number

    def get_column_number(self):
        return self.column_number

    def get_lexeme(self):
        return self.lexeme

    def get_tok_type(self):
        return self.tok_type

