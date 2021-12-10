import sys
from antlr4 import *
from generated.LALGLexer import LALGLexer
from generated.LALGParser import LALGParser
from generated.LALGVisitor import LALGVisitor
from customized.CustomErrorListener import CustomErrorListener
from antlr4.error.ErrorListener import ConsoleErrorListener
from customized.CustomConsoleErrorListener import CustomConsoleErrorListener
from created.SymbolTable import SymbolTable

#ATTENTION: when the grammar rules are changed, you need to generate the grammar files from the command: 
#  java -jar antlr-4.9.2-complete.jar -Dlanguage=Python3 LALG.g4 -visitor -o generated

#Command to run this code (with the virtual enviroment activated):
#  python main.py codes/correto.txt

if __name__ == "__main__":
    data = FileStream(sys.argv[1])
    
    #Analise lexica
    lexer = LALGLexer(data)

    stream = CommonTokenStream(lexer)

    lexer.removeErrorListeners()
    cel = CustomErrorListener()
    lexer.addErrorListener(cel)

    symbolTable = SymbolTable()
    tokens = lexer.getAllTokens()
    for token in tokens:
        symbolTable.insert(token)
    #symbolTable.printSymbolTable()

    cel.printSyntaxErrors()

    lexer.reset()

    #Analise sintatica
    parser = LALGParser(stream)

    parser.removeErrorListeners()
    ccel = CustomConsoleErrorListener()
    parser.addErrorListener(ccel)

    tree = parser.program()
    ccel.printSyntaxErrors()

    #Evaluator
    visitor = LALGVisitor()
    output = visitor.visitProgram(tree)
    print(output)

#Developed by Giovanna Marinho and Guilherme Molina