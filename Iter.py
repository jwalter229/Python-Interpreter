

class Iter:

    def __init__(self, expr1, expr2):
        if expr1 is None or expr2 is None:
            raise ValueError("Null arithmetic expression argument")
        self.expr1 = expr1
        self.expr2 = expr2
        self.it = []

    def evaluate(self):
        self.it.append(self.expr1.evaluate())
        self.it.append(self.expr2.evaluate())
        return self.it

