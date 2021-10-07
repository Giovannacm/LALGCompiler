import sys
from antlr4 import *
from generated.LALGLexer import LALGLexer
from generated.LALGParser import LALGParser
from generated.LALGVisitor import LALGVisitor
from customized.CustomErrorListener import CustomErrorListener

#ATTENTION: when the grammar rules are changed, you need to generate the grammar files from the command: 
#  java -jar antlr-4.9.2-complete.jar -Dlanguage=Python3 LALG.g4 -visitor -o generated

#Command to run this code (with the virtual enviroment activated):
#  python main.py code.txt

if __name__ == "__main__":
    data = FileStream(sys.argv[1])

    cel = CustomErrorListener()

    lexer = LALGLexer(data)
    lexer.removeErrorListeners()
    lexer.addErrorListener(cel)

    tokens = lexer.getAllTokens()

    for token in tokens:
        print(token.text, '->', LALGLexer.ruleNames[token.type - 1])

#Developed by Giovanna Marinho and Guilherme Molina