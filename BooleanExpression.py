from RelativeOperator import RelativeOperator


class BooleanExpression:

    def __init__(self, op, expr1, expr2):
        if op is None:
            raise ValueError("Null relative operator argument")
        if expr1 is None or expr2 is None:
            raise ValueError("Null arithmetic expression argument")
        self.op = op
        self.expr1 = expr1
        self.expr2 = expr2

    def evaluate(self):
        value = False
        if self.op == RelativeOperator.LE_OP:
            value = self.expr1.evaluate() <= self.expr2.evaluate()
        elif self.op == RelativeOperator.LT_OP:
            value = self.expr1.evaluate() < self.expr2.evaluate()
        elif self.op == RelativeOperator.GE_OP:
            value = self.expr1.evaluate() >= self.expr2.evaluate()
        elif self.op == RelativeOperator.GT_OP:
            value = self.expr1.evaluate() > self.expr2.evaluate()
        elif self.op == RelativeOperator.EQ_OP:
            value = self.expr1.evaluate() == self.expr2.evaluate()
        elif self.op == RelativeOperator.NE_OP:
            value = self.expr1.evaluate() != self.expr2.evaluate()
        return value
