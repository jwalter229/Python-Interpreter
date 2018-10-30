from Memory import Memory


class ForStatement:

    def __init__(self, var, it, blk):
        if var is None:
            raise ValueError("Null Id argument")
        if it is None:
            raise ValueError("Null iterator argument")
        if blk is None:
            raise ValueError("Null block argument")
        self.var = var
        self.it = it
        self.blk = blk

    def execute(self):
        # incrementing loop
        if self.it.evaluate()[0] < self.it.evaluate()[1]:
            Memory.store(self.var.get_char(), self.it.evaluate()[0])
            while Memory.fetch(self.var.get_char()) <= self.it.evaluate()[1]:
                self.blk.execute()
                i = Memory.fetch(self.var.get_char())
                i += 1
                Memory.store(self.var.get_char(), i)
        # decrementing loop
        else:
            Memory.store(self.var.get_char(), self.it.evaluate()[0])
            while Memory.fetch(self.var.get_char()) >= self.it.evaluate()[1]:
                self.blk.execute()
                i = Memory.fetch(self.var.get_char())
                i -= 1
                Memory.store(self.var.get_char(), i)
