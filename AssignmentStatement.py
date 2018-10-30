from Memory import Memory


class AssignmentStatement:

    def __init__(self, var, expr):
        if var is None:
            raise ValueError("Null Id argument")
        if expr is None:
            raise ValueError("Null ArithmeticExpression argument")
        self.expr = expr
        self.var = var

    def execute(self):
        Memory.store(self.var.get_char(), self.expr.evaluate())
