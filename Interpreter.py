from Memory import Memory
from Parser import Parser

if __name__ == '__main__':

    files = ["test1.jl", "test2.jl", "test3.jl", "test4.jl"]

    for file in files:
        print('Testing {}'.format(file))
        p = Parser(file)
        program = p.parse()
        program.execute()

        # print tokens and lexemes of the julia file
        # lex = LexicalAnalyzer(file)
        # lex.printLex()

        # to see results of assignment statements
        Memory.display_memory()
        print('Test of {} is complete'.format(file))
        print('******************************************************\n')
        Memory.clear_memory()
