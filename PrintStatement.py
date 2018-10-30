

class PrintStatement:

    def __init__(self, expr):
        super(PrintStatement, self).__init__()
        if expr is None:
            raise ValueError("Null arithmetic expression argument")
        self.expr = expr

    def execute(self):
        print(self.expr.evaluate())
