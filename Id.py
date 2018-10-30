from LexicalAnalyzer import LexicalAnalyzer
from Memory import Memory


class Id:

    def __init__(self, ch):
        if not LexicalAnalyzer.is_valid_identifier(ch):
            raise ValueError("Character is not a valid identifier")
        self.ch = ch

    def evaluate(self):
        return Memory.fetch(self.ch)

    def get_char(self):
        return self.ch
