from antlr4.error.ErrorListener import ErrorListener

class CustomErrorListener(ErrorListener):
    def __init__(self):
        self.syntaxErrors = list()


    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error = {
            'line': line,
            'column': column,
            'msg': msg,
            'exception': e
        }

        self.syntaxErrors.append(error)


    def getSyntaxErrors(self):
        return self.syntaxErrors


    def printSyntaxErrors(self):
        for error in self.syntaxErrors:
            print('Erro em ->', 'Linha:', error['line'], '/ Coluna:', error['column'], '|', error['msg'])