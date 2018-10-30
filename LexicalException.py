

class LexicalException(Exception):

    def __init__(self, string):
        super(LexicalException, self).__init__()
        print(string + "\n")
