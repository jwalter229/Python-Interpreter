from TokenType import TokenType
from LexicalException import LexicalException
from Token import Token


class LexicalAnalyzer:

    def __init__(self, file_name):
        assert file_name is not None
        self.tokens = []
        with open(file_name) as file:
            lines = file.readlines()
            lines = [line.strip() for line in lines]
        for line_number, line in enumerate(lines):
            self.processLine(line, line_number)
        self.tokens.append(Token(line_number, 1, "EOS", TokenType.EOS_TOK))

    def processLine(self, line, line_number):
        assert line is not None and line_number >= 0
        index = 0
        index = LexicalAnalyzer.skip_white_space(line, index)
        while index < len(line):
            lexeme = LexicalAnalyzer.get_lexeme(line, line_number, index)
            tok_type = LexicalAnalyzer.get_token_type(lexeme, line_number, index)
            self.tokens.append(Token(line_number + 1, index + 1, lexeme, tok_type))
            index += len(lexeme)
            index = LexicalAnalyzer.skip_white_space(line, index)

    def get_token_type(lexeme, line_number, column_number):
        assert lexeme is not None and line_number >= 0 and column_number >= 0
        if lexeme[0].isalpha():
            if len(lexeme) == 1:
                if LexicalAnalyzer.is_valid_identifier(lexeme[0]):
                    tok_type = TokenType.ID_TOK
                else:
                    raise LexicalException(
                        "Invalid lexeme at row number {} and column {}".format(line_number + 1, column_number + 1))
            elif lexeme == "if":
                tok_type = TokenType.IF_TOK
            elif lexeme == "function":
                tok_type = TokenType.FUNCTION_TOK
            elif lexeme == "end":
                tok_type = TokenType.END_TOK
            elif lexeme == "else":
                tok_type = TokenType.ELSE_TOK
            elif lexeme == "for":
                tok_type = TokenType.FOR_TOK
            elif lexeme == "while":
                tok_type = TokenType.WHILE_TOK
            elif lexeme == "print":
                tok_type = TokenType.PRINT_TOK
            else:
                raise LexicalException(
                    "Invalid lexeme at row number {} and column {}".format(line_number + 1, column_number + 1))
        elif lexeme[0].isdigit():
            if LexicalAnalyzer.all_digits(lexeme):
                tok_type = TokenType.CONST_TOK
            else:
                raise LexicalException(
                    "Invalid lexeme at row number {} and column {}".format(line_number + 1, column_number + 1))
        elif lexeme == "+":
            tok_type = TokenType.ADD_TOK
        elif lexeme == "-":
            tok_type = TokenType.SUB_TOK
        elif lexeme == "*":
            tok_type = TokenType.MUL_TOK
        elif lexeme == "/":
            tok_type = TokenType.DIV_TOK
        elif lexeme == "\\":
            tok_type = TokenType.REV_DIV_TOK
        elif lexeme == "^":
            tok_type = TokenType.EXP_TOK
        elif lexeme == "%":
            tok_type = TokenType.MOD_TOK
        elif lexeme == "=":
            tok_type = TokenType.ASSIGN_TOK
        elif lexeme == "(":
            tok_type = TokenType.LEFT_PAREN_TOK
        elif lexeme == ")":
            tok_type = TokenType.RIGHT_PAREN_TOK
        elif lexeme == ">=":
            tok_type = TokenType.GE_TOK
        elif lexeme == ">":
            tok_type = TokenType.GT_TOK
        elif lexeme == "<=":
            tok_type = TokenType.LE_TOK
        elif lexeme == "<":
            tok_type = TokenType.LT_TOK
        elif lexeme == "==":
            tok_type = TokenType.EQ_TOK
        elif lexeme == "!=":
            tok_type = TokenType.NE_TOK
        elif lexeme == ":":
            tok_type = TokenType.COL_TOK
        else:
            raise LexicalException(
                "Invalid lexeme at row number {} and column {}".format(line_number + 1, column_number + 1))
        return tok_type

    def all_digits(self):
        assert self is not None
        i = 0
        while i < len(self) and self[i].isdigit():
            i += 1
        return i == len(self)

    def get_lexeme(line, line_number, index):
        assert line is not None and line_number >= 0 and index >= 0
        i = index
        while i < len(line):
            if line[i].isspace():
                break
            i += 1
        return line[index:i]

    def skip_white_space(line, index):
        assert line is not None and index >= 0
        i = index
        while i < len(line):
            if not line[i].isspace():
                break
            i += 1
        return i

    def get_next_token(self):
        if not len(self.tokens):
            raise LexicalException("No more tokens")
        return self.tokens.pop(0)

    def get_lookahead_token(self):
        if not len(self.tokens):
            raise LexicalException("No more tokens")
        return self.tokens[0]

    def is_valid_identifier(self):
        return self.isalpha()

    # print all tokens and lexemes
    def print_lex(self):
        for token in self.tokens:
            tok_type = token.get_tok_type()
            lexeme = token.get_lexeme()
            print("The next token is: " + str(tok_type) + " **** Next lexeme is: " + str(lexeme))
