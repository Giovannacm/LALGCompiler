from antlr4.error.ErrorListener import ErrorListener
from antlr4 import Token

class CustomErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
    	print('Erro em ->', 'Linha:', line, '/ Coluna:', column, '|', msg)