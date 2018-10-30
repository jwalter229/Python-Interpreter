from LexicalAnalyzer import LexicalAnalyzer


class Memory:
    mem = [None] * 52

    def fetch(self):
        return Memory.mem[Memory.getIndex(self)]

    def store(self, value):
        Memory.mem[Memory.getIndex(self)] = value

    def getIndex(ch):
        if not LexicalAnalyzer.is_valid_identifier(ch):
            raise ValueError(ch + " is not a valid identifier")
        if ord(ch) - ord('A') < 26:
            return ord(ch) - ord('A')
        else:
            return ord(ch) - ord('a') + 26

    def display_memory():
        for i, v in enumerate(Memory.mem):
            if i < 26:
                print('{}: {}'.format(chr(ord('A') + i), str(v)))
            else:
                print('{}: {}'.format(chr(ord('a') + i - 26), str(v)))

    def clear_memory():
        Memory.mem = [None] * 52
