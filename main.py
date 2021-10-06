import sys
from antlr4 import *
from generated.LALGGrammarLexer import LALGGrammarLexer
from generated.LALGGrammarParser import LALGGrammarParser
from generated.LALGGrammarVisitor import LALGGrammarVisitor

#ATTENTION: when the grammar rules are changed, you need to generate the grammar files from the command: 
#  java -jar antlr-4.9.2-complete.jar -Dlanguage=Python3 LALGGrammar.g4 -visitor -o generated

if __name__ == "__main__":
    data = FileStream(sys.argv[1])

    lexer = LALGGrammarLexer(data)

    tokens = lexer.getAllTokens()

    for token in tokens:
        print(token.text, '->', LALGGrammarLexer.ruleNames[token.type - 1])