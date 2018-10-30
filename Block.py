

class Block:

    def __init__(self):
        self.statements = []

    def add(self, statement):
        if statement is None:
            raise ValueError("Null statement argument")
        self.statements.append(statement)

    def execute(self):
        for statement in self.statements:
            statement.execute()
