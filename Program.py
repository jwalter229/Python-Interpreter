

class Program:

    def __init__(self, blk):
        if blk is None:
            raise ValueError("Null block argument")
        self.blk = blk

    def execute(self):
        self.blk.execute()
