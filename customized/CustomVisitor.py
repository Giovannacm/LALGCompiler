from generated.LALGVisitor import LALGVisitor
from generated.LALGParser import LALGParser
from created.SemanticUtil import SemanticUtil
from created.VisitorSymbolTable import VisitorSymbolTable
from created.VisitorSymbolTable import Type


class CustomVisitor(LALGVisitor):

	# Visit a parse tree produced by LALGParser#program.
	def visitProgram(self, ctx:LALGParser.ProgramContext):
		self.scopeTable = list()
		self.scope = -1
		return self.visitChildren(ctx)


	# Visit a parse tree produced by LALGParser#block.
	def visitBlock(self, ctx:LALGParser.BlockContext):
		self.table = VisitorSymbolTable()
		return self.visitChildren(ctx)


	# Visit a parse tree produced by LALGParser#variableDeclarationPart.
	def visitVariableDeclarationPart(self, ctx:LALGParser.VariableDeclarationPartContext):
		self.scope += 1
		self.scopeTable.append(self.table)
		return self.visitChildren(ctx)


	# Visit a parse tree produced by LALGParser#variableDeclaration.
	def visitVariableDeclaration(self, ctx:LALGParser.VariableDeclarationContext):
		varTypeStr = ctx.simpleType().getText()
		varType = Type.INVALID

		if (varTypeStr == 'int'):
			varType = Type.INTEGER
		elif (varTypeStr == 'real'):
			varType = Type.REAL
		elif (varTypeStr == 'boolean'):
			varType = Type.BOOLEAN

		variables = ctx.identifierList().identifier()

		for variable in variables:
			varName = variable.getText()
			#print(variable.getText())

			if (self.scopeTable[self.scope].existsSymbol(varName)):
				SemanticUtil.insertError(variable.start, "Variavel " + varName + " ja declarada")
			else:
				self.scopeTable[self.scope].insert(varName, varType)

		return self.visitChildren(ctx)


	# Visit a parse tree produced by LALGParser#assignmentStatement.
	def visitAssignmentStatement(self, ctx:LALGParser.AssignmentStatementContext):
		expessionType = SemanticUtil.verifyType(self.scopeTable[self.scope], ctx.expression())

		if (expessionType != Type.INVALID):
			varName = ctx.variable().getText()

			if (not self.scopeTable[self.scope].existsSymbol(varName)):
				SemanticUtil.insertError(ctx.start, "Variavel " + varName + " nao foi declarada antes do uso")
			else:
				varType = SemanticUtil.verifyType(self.scopeTable[self.scope], varName)
				if (varType != expessionType):
					SemanticUtil.insertError(ctx.start, "Tipo da variavel " + varName + " nao e compativel com o tipo da expressao")

		return self.visitChildren(ctx)
	

	# Visit a parse tree produced by LALGParser#expression.
	def visitExpression(self, ctx:LALGParser.ExpressionContext):
		SemanticUtil.verifyType(self.scopeTable[self.scope], ctx)
		return self.visitChildren(ctx)