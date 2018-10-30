

class WhileStatement:

    def __init__(self, expr, blk):
        if expr is None:
            raise ValueError("Null boolean expression argument")
        if blk is None:
            raise ValueError("Null block argument")
        self.expr = expr
        self.blk = blk

    def execute(self):
        while self.expr.evaluate():
            self.blk.execute()
