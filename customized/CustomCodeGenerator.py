from generated.LALGVisitor import LALGVisitor
from generated.LALGParser import LALGParser
from created.SemanticUtil import SemanticUtil
from created.VisitorSymbolTable import VisitorSymbolTable
from created.VisitorSymbolTable import Type


class CustomCodeGenerator(LALGVisitor):
	def getVariablesValues(self):
		for i in range(0, self.scope+1):
			print('\nScope: ' + str(i))

			for variable in self.scopeTable[i]:
				print(variable['name'] + ': ' + str(variable['value']))


	def getVariableValue(self, scope, name):
		for variable in self.scopeTable[scope]:
			if variable['name'] == name:
				print(variable['name'] + ': ' + str(variable['value']))


	def setVariableValue(self, scope, name, value):
		for variable in self.scopeTable[scope]:
			if variable['name'] == name:
				variable['value'] = value


	# Visit a parse tree produced by LALGParser#program.
	def visitProgram(self, ctx:LALGParser.ProgramContext):
		self.scopeTable = list()
		self.scope = -1
		return self.visitChildren(ctx)


	# Visit a parse tree produced by LALGParser#block.
	def visitBlock(self, ctx:LALGParser.BlockContext):
		self.table = list()
		return self.visitChildren(ctx)


	# Visit a parse tree produced by LALGParser#variableDeclarationPart.
	def visitVariableDeclarationPart(self, ctx:LALGParser.VariableDeclarationPartContext):
		self.scope += 1
		self.scopeTable.append(self.table)
		return self.visitChildren(ctx)


	# Visit a parse tree produced by LALGParser#variableDeclaration.
	def visitVariableDeclaration(self, ctx:LALGParser.VariableDeclarationContext):
		variables = ctx.identifierList().identifier()

		for variable in variables:
			varName = variable.getText()
			self.scopeTable[self.scope].append({'name': varName, 'value': None})

		return self.visitChildren(ctx)


	# Visit a parse tree produced by LALGParser#assignmentStatement.
	def visitAssignmentStatement(self, ctx:LALGParser.AssignmentStatementContext):
		expessionValue = self.customVisitExpression(ctx.expression())
		varName = ctx.variable().getText()
		
		for variable in self.scopeTable[self.scope]:
			if variable['name'] == varName:
				variable['value'] = expessionValue
		
		return self.visitChildren(ctx)


	# Visit a parse tree produced by LALGParser#conditionalStatement.
	def visitConditionalStatement(self, ctx:LALGParser.ConditionalStatementContext):
		#conditionalStatement: (IF expression statement ELSE statement) | (IF expression statement) ;
		if(len(ctx.statement()) > 1): #tem else
			expressionValue = self.customVisitExpression(ctx.expression()[0])

			if (expressionValue):
				return self.customVisitStatement(ctx.statement()[0])
			else:
				return self.customVisitStatement(ctx.statement()[1])
		else:
			expressionValue = self.customVisitExpression(ctx.expression())
			if (expressionValue):
				return self.customVisitStatement(ctx.statement()[0])


	# Visit a parse tree produced by LALGParser#repetetiveStatement.
	def visitRepetetiveStatement(self, ctx:LALGParser.RepetetiveStatementContext):
		#repetetiveStatement: WHILE expression statement ; 

		expressionResult = self.customVisitExpression(ctx.expression())
		while (expressionResult):
			self.customVisitStatement(ctx.statement())
			expressionResult = self.customVisitExpression(ctx.expression())


	# Visit a parse tree produced by LALGParser#compoundStatement.
	def visitCompoundStatement(self, ctx:LALGParser.CompoundStatementContext):
		for statement in ctx.statement():
			self.customVisitStatement(statement)
	

	# Visit a parse tree produced by LALGParser#procedureStatement.
	def visitProcedureStatement(self, ctx:LALGParser.ProcedureStatementContext):
		if ctx.identifier().getText() == 'write':
			print('> ' + str(self.getVariableValue(self.scope, ctx.expressionList().expression()[0])))
		elif ctx.identifier().getText() == 'read':
			value = int(input('< '))
			self.setVariableValue(self.scope, ctx.expressionList().expression()[0], value)
		return self.visitChildren(ctx)


	def customVisitStatement(self, ctx:LALGParser.StatementContext):
		if ctx.assignmentStatement():
			return self.visitAssignmentStatement(ctx.assignmentStatement())
		elif ctx.compoundStatement():
			return self.visitCompoundStatement(ctx.compoundStatement())
		elif ctx.conditionalStatement():
			return self.visitConditionalStatement(ctx.conditionalStatement())
		elif ctx.repetetiveStatement():
			return self.visitRepetetiveStatement(ctx.repetetiveStatement())
		return self.visitChildren(ctx)


	def customVisitExpression(self, ctx:LALGParser.ExpressionContext):
		if ctx.TRUE() != None:
			return True

		if ctx.FALSE() != None:
			return False

		if ctx.relationalOperator() != None:
			acc = 0
			op = ctx.relationalOperator()
			expressions = ctx.simpleExpression()
			for i in range(0, len(expressions), 2):
				result1 = self.customVisitSimpleExpression(expressions[i])
				result2 = self.customVisitSimpleExpression(expressions[i + 1])

				if op.GT():
					acc = result1 > result2
				elif op.GE():
					acc = result1 >= result2
				elif op.LT():
					acc = result1 < result2
				elif op.LE():
					acc = result1 <= result2
				elif op.NOT_EQUAL():
					acc = result1 != result2
				else: #EQUAL
					acc = result1 == result2
			return acc

		result = 0
		for expression in ctx.simpleExpression():
			result = self.customVisitSimpleExpression(expression)

		return result


	def customVisitSimpleExpression(self, ctx:LALGParser.SimpleExpressionContext):

		if len(ctx.additiveOperator()) != 0:
			acc = 0
			op = ctx.additiveOperator()[0]
			terms = ctx.term()
			for i in range(0, len(terms), 2):
				result1 = self.customVisitTerm(terms[i])
				result2 = self.customVisitTerm(terms[i + 1])

				if op.PLUS():
					acc = result1 + result2
				elif op.MINUS():
					acc = result1 - result2
				else: #OR
					acc = result1 or result2

			return acc
		
		return self.customVisitTerm(ctx.term()[0])


	def customVisitTerm(self, ctx:LALGParser.TermContext):
		if len(ctx.multiplicativeOperator()) != 0:
			acc = 1
			op = ctx.multiplicativeOperator()[0]
			factors = ctx.factor()
			for i in range(0, len(factors), 2):
				result1 = self.customVisitFactor(factors[i])
				result2 = self.customVisitFactor(factors[i + 1])

				if op.STAR():
					acc = result1 * result2
				elif op.DIV():
					acc = result1 / result2
				else: #AND
					acc = result1 and result2

			return acc

		return self.customVisitFactor(ctx.factor()[0])


	def customVisitFactor(self, ctx:LALGParser.FactorContext):
		if ctx.variable() != None:
			for variable in self.scopeTable[self.scope]:
				if variable['name'] == ctx.variable().getText():
					return variable['value']
		elif ctx.unsignedNumber() != None:
			if ctx.unsignedNumber().NUMINT() != None:
				return int(ctx.unsignedNumber().getText())
			if ctx.unsignedNumber().NUMREAL() != None:
				return float(ctx.unsignedNumber().getText())
		elif ctx.expression() != None:
			return self.customVisitExpression(ctx.expression())

		return self.customVisitFactor(ctx.factor())