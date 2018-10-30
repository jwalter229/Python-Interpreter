

class IfStatement:

    def __init__(self, expr, blk1, blk2):
        if expr is None:
            raise ValueError("Null boolean expression argument")
        if blk1 is None or blk2 is None:
            raise ValueError("Null block argument")
        self.expr = expr
        self.blk1 = blk1
        self.blk2 = blk2

    def execute(self):
        if self.expr.evaluate():
            self.blk1.execute()
        else:
            self.blk2.execute()
