# Generated from LALG.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LALGParser import LALGParser
else:
    from LALGParser import LALGParser

# This class defines a complete generic visitor for a parse tree produced by LALGParser.

class LALGVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LALGParser#program.
    def visitProgram(self, ctx:LALGParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LALGParser#block.
    def visitBlock(self, ctx:LALGParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LALGParser#variableDeclarationPart.
    def visitVariableDeclarationPart(self, ctx:LALGParser.VariableDeclarationPartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LALGParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:LALGParser.VariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LALGParser#simpleType.
    def visitSimpleType(self, ctx:LALGParser.SimpleTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LALGParser#identifierList.
    def visitIdentifierList(self, ctx:LALGParser.IdentifierListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LALGParser#procedureDeclarationPart.
    def visitProcedureDeclarationPart(self, ctx:LALGParser.ProcedureDeclarationPartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LALGParser#procedureDeclaration.
    def visitProcedureDeclaration(self, ctx:LALGParser.ProcedureDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LALGParser#formalParameter.
    def visitFormalParameter(self, ctx:LALGParser.FormalParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LALGParser#formalParameterSection.
    def visitFormalParameterSection(self, ctx:LALGParser.FormalParameterSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LALGParser#compoundStatement.
    def visitCompoundStatement(self, ctx:LALGParser.CompoundStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LALGParser#statement.
    def visitStatement(self, ctx:LALGParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LALGParser#assignmentStatement.
    def visitAssignmentStatement(self, ctx:LALGParser.AssignmentStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LALGParser#procedureStatement.
    def visitProcedureStatement(self, ctx:LALGParser.ProcedureStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LALGParser#conditionalStatement.
    def visitConditionalStatement(self, ctx:LALGParser.ConditionalStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LALGParser#repetetiveStatement.
    def visitRepetetiveStatement(self, ctx:LALGParser.RepetetiveStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LALGParser#expression.
    def visitExpression(self, ctx:LALGParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LALGParser#relationalOperator.
    def visitRelationalOperator(self, ctx:LALGParser.RelationalOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LALGParser#simpleExpression.
    def visitSimpleExpression(self, ctx:LALGParser.SimpleExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LALGParser#additiveOperator.
    def visitAdditiveOperator(self, ctx:LALGParser.AdditiveOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LALGParser#term.
    def visitTerm(self, ctx:LALGParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LALGParser#multiplicativeOperator.
    def visitMultiplicativeOperator(self, ctx:LALGParser.MultiplicativeOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LALGParser#factor.
    def visitFactor(self, ctx:LALGParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LALGParser#unsignedNumber.
    def visitUnsignedNumber(self, ctx:LALGParser.UnsignedNumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LALGParser#variable.
    def visitVariable(self, ctx:LALGParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LALGParser#expressionList.
    def visitExpressionList(self, ctx:LALGParser.ExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LALGParser#identifier.
    def visitIdentifier(self, ctx:LALGParser.IdentifierContext):
        return self.visitChildren(ctx)



del LALGParser