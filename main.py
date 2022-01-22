import sys
from antlr4 import *
from generated.LALGLexer import LALGLexer
from generated.LALGParser import LALGParser
from generated.LALGVisitor import LALGVisitor
from customized.CustomErrorListener import CustomErrorListener
from antlr4.error.ErrorListener import ConsoleErrorListener
from customized.CustomConsoleErrorListener import CustomConsoleErrorListener
from created.SymbolTable import SymbolTable
from customized.CustomVisitor import CustomVisitor
from customized.CustomCodeGenerator import CustomCodeGenerator
from created.SemanticUtil import SemanticUtil


#ATTENTION: when the grammar rules are changed, you need to generate the grammar files from the command: 
#  java -jar antlr-4.9.2-complete.jar -Dlanguage=Python3 LALG.g4 -visitor -o generated

#Command to run this code (with the virtual enviroment activated):
#  python main.py codes/correto.txt

#TO-DO
#   scopo
#   leitura (ver o tipo)


def compressErrors(lexicon, syntactic, semantic):
    errors = list()
    errors.append({'type': 'lexicon', 'error': lexicon})
    errors.append({'type': 'syntactic', 'error': syntactic})
    errors.append({'type': 'semantic', 'error': semantic})
    return errors
    

def success(errors):
    for error in errors:
        if len(error['error']) > 0:
            return False
    return True


def printErrors(errors):
    for error in errors:
        print('\n' + error['type'])
        for item in error['error']:
            print('Erro em ->', 'Linha:', item['line'], '/ Coluna:', item['column'], '|', item['msg'])


if __name__ == "__main__":
    data = FileStream(sys.argv[1])
    
    #Analise lexica
    print('Analise lexica')
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

    #cel.printSyntaxErrors()

    lexer.reset()

    #Analise sintatica
    print('Analise sintatica')
    parser = LALGParser(stream)

    parser.removeErrorListeners()
    ccel = CustomConsoleErrorListener()
    parser.addErrorListener(ccel)

    tree = parser.program()
    #ccel.printSyntaxErrors()

    #Evaluator - Analise semantica - Esquemas de Traducao Dirigida pela Sintaxe (TDS)
    print('Analise semantica')
    visitor = CustomVisitor()
    output = visitor.visitProgram(tree)

    errors = compressErrors(cel.getSyntaxErrors(), ccel.getSyntaxErrors(), SemanticUtil.getSemanticalErrors())

    if not success(errors):
        #SemanticUtil.printSemanticalErrors()
        printErrors(errors)
    else:
        codeGenerator = CustomCodeGenerator()
        output = codeGenerator.visitProgram(tree)
        codeGenerator.getVariablesValues()

#Developed by Giovanna Marinho and Guilherme Molina