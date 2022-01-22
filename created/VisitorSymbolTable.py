from enum import Enum


class Type(Enum):
	INTEGER = 1 
	REAL = 2
	BOOLEAN = 3
	INVALID = 4


class VisitorSymbolTable():
	
	def __init__(self):
		self.table = list()


	def insert(self, name, stype):
		symbol = {
			'name': name, 
			'type': stype
		}

		self.table.append(symbol)


	def existsSymbol(self, name):
		return not(len([symbol for symbol in self.table if symbol['name'] == name]) == 0)


	def getSymbolType(self, name):
		return [symbol for symbol in self.table if symbol['name'] == name][0]['type']
