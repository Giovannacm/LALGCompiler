from generated.LALGParser import LALGParser
from created.VisitorSymbolTable import Type

class SemanticUtil:
	semanticalErrors = list()

	@staticmethod
	def insertError(ctx, msg):
		error = {
			'line': ctx.line,
			'column': ctx.column,
			'msg': msg
		}

		SemanticUtil.semanticalErrors.append(error)
		
	@staticmethod
	def verifyType(symbolTable, ctx):
		if isinstance(ctx, LALGParser.ExpressionContext):
			aux = SemanticUtil.verifyExpressionContextType(symbolTable, ctx)
		elif isinstance(ctx, LALGParser.TermContext):
			aux = SemanticUtil.verifyTermContextType(symbolTable, ctx)
		elif isinstance(ctx, LALGParser.FactorContext):
			aux = SemanticUtil.verifyFactorContextType(symbolTable, ctx)
		elif isinstance(ctx, str):
			aux = SemanticUtil.verifyStrType(symbolTable, ctx)

		return aux

	@staticmethod
	def verifyExpressionContextType(symbolTable, ctx:LALGParser.ExpressionContext):
		if (ctx.TRUE() != None) or (ctx.FALSE() != None): 
			ret = Type.BOOLEAN

		elif (ctx.simpleExpression() != None):
			simp = ctx.simpleExpression()[0].term()

			ret = None
			for ta in simp:
				aux = SemanticUtil.verifyType(symbolTable, ta)

				if (ret == None):
					ret = aux
				elif (ret != aux) and (aux != Type.INVALID):
					SemanticUtil.insertError(ctx.start, "Expressao " + ctx.getText() + " contem tipos incompativeis")
					ret = Type.INVALID

		return ret

	@staticmethod
	def verifyTermContextType(symbolTable, ctx:LALGParser.TermContext):
		ret = None

		for fa in ctx.factor():
			aux = SemanticUtil.verifyType(symbolTable, fa)

			if (ret == None):
				ret = aux
			elif (ret != aux) and (aux != Type.INVALID):
				SemanticUtil.insertError(ctx.start, "Termo " + ctx.getText() + " contem tipos incompativeis")
				ret = Type.INVALID

		return ret

	@staticmethod
	def verifyFactorContextType(symbolTable, ctx:LALGParser.FactorContext):
		
		if (ctx.unsignedNumber() != None):
			if(ctx.unsignedNumber().NUMINT() != None):
				return Type.INTEGER

			if(ctx.unsignedNumber().NUMREAL() != None):
				return Type.REAL

		if (ctx.variable() != None):
			varName = ctx.variable().getText()

			if(not symbolTable.existsSymbol(varName)):
				SemanticUtil.insertError(ctx.start, "Variavel " + varName + " nao foi declarada antes do uso")
				return Type.INVALID

			return SemanticUtil.verifyType(symbolTable, varName)

		if (ctx.factor() != None):
			return SemanticUtil.verifyType(symbolTable, ctx.factor())

		return SemanticUtil.verifyType(symbolTable, ctx.expression())

	@staticmethod
	def verifyStrType(symbolTable, varName:str):
		return symbolTable.getSymbolType(varName)

	@staticmethod
	def getSemanticalErrors():
		return SemanticUtil.semanticalErrors

	@staticmethod
	def printSemanticalErrors():
		for error in SemanticUtil.semanticalErrors:
			print('Erro em ->', 'Linha:', error['line'], '/ Coluna:', error['column'], '|', error['msg'])
