

class ParserException(Exception):

    def __init__(self, string):
        super(ParserException, self).__init__()
        print(string + "\n")

