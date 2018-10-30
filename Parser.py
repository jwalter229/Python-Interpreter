from TokenType import TokenType
from ArithmeticOperator import ArithmeticOperator
from AssignmentStatement import AssignmentStatement
from BinaryExpression import BinaryExpression
from Block import Block
from BooleanExpression import BooleanExpression
from Constant import Constant
from ForStatement import ForStatement
from Id import Id
from IfStatement import IfStatement
from Iter import Iter
from LexicalAnalyzer import LexicalAnalyzer
from PrintStatement import PrintStatement
from Program import Program
from RelativeOperator import RelativeOperator
from WhileStatement import WhileStatement


class Parser:

    def __init__(self, file_name):
        self.lex = LexicalAnalyzer(file_name)

    def parse(self):
        tok = self.lex.get_next_token()
        Parser.match(tok, TokenType.FUNCTION_TOK)
        functionName = self.get_id()
        tok = self.lex.get_next_token()
        Parser.match(tok, TokenType.LEFT_PAREN_TOK)
        tok = self.lex.get_next_token()
        Parser.match(tok, TokenType.RIGHT_PAREN_TOK)
        blk = self.get_block()
        tok = self.lex.get_next_token()
        Parser.match(tok, TokenType.END_TOK)
        tok = self.lex.get_next_token()
        if tok.get_tok_type() != TokenType.EOS_TOK:
            raise Exception("garbage at end of file")
        return Program(blk)

    def get_block(self):
        blk = Block()
        tok = self.lex.get_lookahead_token()
        while Parser.is_valid_start_of_statement(tok):
            stmt = self.get_statement()
            blk.add(stmt)
            tok = self.lex.get_lookahead_token()
        return blk

    def get_statement(self):
        tok = self.lex.get_lookahead_token()
        if tok.get_tok_type() == TokenType.IF_TOK:
            stmt = self.get_if_statement()
        elif tok.get_tok_type() == TokenType.WHILE_TOK:
            stmt = self.get_while_statement()
        elif tok.get_tok_type() == TokenType.PRINT_TOK:
            stmt = self.get_print_statement()
        elif tok.get_tok_type() == TokenType.ID_TOK:
            stmt = self.get_assignment_statement()
        elif tok.get_tok_type() == TokenType.FOR_TOK:
            stmt = self.get_for_statement()
        else:
            raise Exception(
                "invalid statement at row " + tok.get_row_number() + " and column " + tok.get_column_number())
        return stmt

    def get_assignment_statement(self):
        var = self.get_id()
        tok = self.lex.get_next_token()
        Parser.match(tok, TokenType.ASSIGN_TOK)
        expr = self.get_arithmetic_expression()
        return AssignmentStatement(var, expr)

    def get_print_statement(self):
        tok = self.lex.get_next_token()
        Parser.match(tok, TokenType.PRINT_TOK)
        tok = self.lex.get_next_token()
        Parser.match(tok, TokenType.LEFT_PAREN_TOK)
        expr = self.get_arithmetic_expression()
        tok = self.lex.get_next_token()
        Parser.match(tok, TokenType.RIGHT_PAREN_TOK)
        return PrintStatement(expr)

    def get_for_statement(self):
        tok = self.lex.get_next_token()
        Parser.match(tok, TokenType.FOR_TOK)
        var = self.get_id()
        tok = self.lex.get_next_token()
        Parser.match(tok, TokenType.ASSIGN_TOK)
        expr1 = self.get_arithmetic_expression()
        tok = self.lex.get_next_token()
        Parser.match(tok, TokenType.COL_TOK)
        expr2 = self.get_arithmetic_expression()
        blk = self.get_block()
        tok = self.lex.get_next_token()
        Parser.match(tok, TokenType.END_TOK)
        it = Iter(expr1, expr2)
        return ForStatement(var, it, blk)

    def get_while_statement(self):
        tok = self.lex.get_next_token()
        Parser.match(tok, TokenType.WHILE_TOK)
        expr = self.get_boolean_expression()
        blk = self.get_block()
        tok = self.lex.get_next_token()
        Parser.match(tok, TokenType.END_TOK)
        return WhileStatement(expr, blk)

    def get_if_statement(self):
        tok = self.lex.get_next_token()
        Parser.match(tok, TokenType.IF_TOK)
        expr = self.get_boolean_expression()
        blk1 = self.get_block()
        tok = self.lex.get_next_token()
        Parser.match(tok, TokenType.ELSE_TOK)
        blk2 = self.get_block()
        tok = self.lex.get_next_token()
        Parser.match(tok, TokenType.END_TOK)
        return IfStatement(expr, blk1, blk2)

    def is_valid_start_of_statement(tok):
        assert (tok is not None)
        return tok.get_tok_type() == TokenType.ID_TOK or tok.get_tok_type() == TokenType.IF_TOK \
               or tok.get_tok_type() == TokenType.WHILE_TOK or tok.get_tok_type() == TokenType.FOR_TOK \
               or tok.get_tok_type() == TokenType.PRINT_TOK

    def get_arithmetic_expression(self):
        tok = self.lex.get_lookahead_token()
        if tok.get_tok_type() == TokenType.ID_TOK:
            expr = self.get_id()
        elif tok.get_tok_type() == TokenType.CONST_TOK:
            expr = self.get_constant()
        else:
            expr = self.get_binary_expression()
        return expr

    def get_binary_expression(self):
        tok = self.lex.get_next_token()
        if tok.get_tok_type() == TokenType.ADD_TOK:
            Parser.match(tok, TokenType.ADD_TOK)
            op = ArithmeticOperator.ADD_OP
        elif tok.get_tok_type() == TokenType.SUB_TOK:
            Parser.match(tok, TokenType.SUB_TOK)
            op = ArithmeticOperator.SUB_OP
        elif tok.get_tok_type() == TokenType.MUL_TOK:
            Parser.match(tok, TokenType.MUL_TOK)
            op = ArithmeticOperator.MUL_OP
        elif tok.get_tok_type() == TokenType.DIV_TOK:
            Parser.match(tok, TokenType.DIV_TOK)
            op = ArithmeticOperator.DIV_OP
        elif tok.get_tok_type() == TokenType.REV_DIV_TOK:
            Parser.match(tok, TokenType.REV_DIV_TOK)
            op = ArithmeticOperator.REV_DIV_OP
        elif tok.get_tok_type() == TokenType.EXP_TOK:
            Parser.match(tok, TokenType.EXP_TOK)
            op = ArithmeticOperator.EXP_OP
        elif tok.get_tok_type() == TokenType.MOD_TOK:
            Parser.match(tok, TokenType.MOD_TOK)
            op = ArithmeticOperator.MOD_OP
        else:
            raise Exception(
                " operator expected at row " + tok.get_row_number() + " and column " + tok.get_column_number())
        expr1 = self.get_arithmetic_expression()
        expr2 = self.get_arithmetic_expression()
        return BinaryExpression(op, expr1, expr2)

    def get_boolean_expression(self):
        tok = self.lex.get_next_token()
        if tok.get_tok_type() == TokenType.EQ_TOK:
            op = RelativeOperator.EQ_OP
        elif tok.get_tok_type() == TokenType.NE_TOK:
            op = RelativeOperator.NE_OP
        elif tok.get_tok_type() == TokenType.GT_TOK:
            op = RelativeOperator.GT_OP
        elif tok.get_tok_type() == TokenType.GE_TOK:
            op = RelativeOperator.GE_OP
        elif tok.get_tok_type() == TokenType.LT_TOK:
            op = RelativeOperator.LT_OP
        elif tok.get_tok_type() == TokenType.LE_TOK:
            op = RelativeOperator.LE_OP
        else:
            raise Exception(
                "relational operator expected at row " + tok.get_row_number() + " and column " + tok.get_column_number())
        expr1 = self.get_arithmetic_expression()
        expr2 = self.get_arithmetic_expression()
        return BooleanExpression(op, expr1, expr2)

    def get_id(self):
        tok = self.lex.get_next_token()
        Parser.match(tok, TokenType.ID_TOK)
        return Id(tok.get_lexeme()[0])

    def get_constant(self):
        tok = self.lex.get_next_token()
        Parser.match(tok, TokenType.CONST_TOK)
        value = int(tok.get_lexeme())
        return Constant(value)

    def match(tok, tok_type):
        assert (tok is not None and tok_type is not None)
        if tok.get_tok_type() != tok_type:
            raise Exception(
                tok_type.name() + " expected at row " + tok.get_row_number() + " and column " + tok.get_column_number())
