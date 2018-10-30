from ArithmeticOperator import ArithmeticOperator


class BinaryExpression:

    def __init__(self, op, expr1, expr2):
        if op is None:
            raise ValueError("Null arithmetic operator argument")
        if expr1 is None or expr2 is None:
            raise ValueError("Null expression argument")
        self.expr1 = expr1
        self.expr2 = expr2
        self.op = op

    def evaluate(self):
        value = 0
        if self.op == ArithmeticOperator.ADD_OP:
            value = self.expr1.evaluate() + self.expr2.evaluate()
        elif self.op == ArithmeticOperator.SUB_OP:
            value = self.expr1.evaluate() - self.expr2.evaluate()
        elif self.op == ArithmeticOperator.MUL_OP:
            value = self.expr1.evaluate() * self.expr2.evaluate()
        elif self.op == ArithmeticOperator.DIV_OP:
            value = self.expr1.evaluate() / self.expr2.evaluate()
        elif self.op == ArithmeticOperator.MOD_OP:
            value = self.expr1.evaluate() % self.expr2.evaluate()
        elif self.op == ArithmeticOperator.EXP_OP:
            value = self.expr1.evaluate() ** self.expr2.evaluate()
        elif self.op == ArithmeticOperator.REV_DIV_OP:
            value = self.expr2.evaluate() / self.expr1.evaluate()
        return value
