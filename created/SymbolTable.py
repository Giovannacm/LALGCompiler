from generated.LALGLexer import LALGLexer


class SymbolTable():
	def __init__(self):
		self.table = list()


	def insert(self, token):
		symbol = {
			'token': LALGLexer.ruleNames[token.type - 1], 
			'lexeme': token.text, 
			'start': token.start,
			'stop': token.stop,
			'line': token.line , 
			'column': token.column
		}

		self.table.append(symbol)


	def getSymbolTable(self):
		return self.table


	def printSymbolTable(self):
		for symbol in self.table:
			print(symbol)