# Generated from LALG.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LALGParser import LALGParser
else:
    from LALGParser import LALGParser

# This class defines a complete listener for a parse tree produced by LALGParser.
class LALGListener(ParseTreeListener):

    # Enter a parse tree produced by LALGParser#program.
    def enterProgram(self, ctx:LALGParser.ProgramContext):
        pass

    # Exit a parse tree produced by LALGParser#program.
    def exitProgram(self, ctx:LALGParser.ProgramContext):
        pass


    # Enter a parse tree produced by LALGParser#block.
    def enterBlock(self, ctx:LALGParser.BlockContext):
        pass

    # Exit a parse tree produced by LALGParser#block.
    def exitBlock(self, ctx:LALGParser.BlockContext):
        pass


    # Enter a parse tree produced by LALGParser#variableDeclarationPart.
    def enterVariableDeclarationPart(self, ctx:LALGParser.VariableDeclarationPartContext):
        pass

    # Exit a parse tree produced by LALGParser#variableDeclarationPart.
    def exitVariableDeclarationPart(self, ctx:LALGParser.VariableDeclarationPartContext):
        pass


    # Enter a parse tree produced by LALGParser#variableDeclaration.
    def enterVariableDeclaration(self, ctx:LALGParser.VariableDeclarationContext):
        pass

    # Exit a parse tree produced by LALGParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx:LALGParser.VariableDeclarationContext):
        pass


    # Enter a parse tree produced by LALGParser#simpleType.
    def enterSimpleType(self, ctx:LALGParser.SimpleTypeContext):
        pass

    # Exit a parse tree produced by LALGParser#simpleType.
    def exitSimpleType(self, ctx:LALGParser.SimpleTypeContext):
        pass


    # Enter a parse tree produced by LALGParser#identifierList.
    def enterIdentifierList(self, ctx:LALGParser.IdentifierListContext):
        pass

    # Exit a parse tree produced by LALGParser#identifierList.
    def exitIdentifierList(self, ctx:LALGParser.IdentifierListContext):
        pass


    # Enter a parse tree produced by LALGParser#procedureDeclarationPart.
    def enterProcedureDeclarationPart(self, ctx:LALGParser.ProcedureDeclarationPartContext):
        pass

    # Exit a parse tree produced by LALGParser#procedureDeclarationPart.
    def exitProcedureDeclarationPart(self, ctx:LALGParser.ProcedureDeclarationPartContext):
        pass


    # Enter a parse tree produced by LALGParser#procedureDeclaration.
    def enterProcedureDeclaration(self, ctx:LALGParser.ProcedureDeclarationContext):
        pass

    # Exit a parse tree produced by LALGParser#procedureDeclaration.
    def exitProcedureDeclaration(self, ctx:LALGParser.ProcedureDeclarationContext):
        pass


    # Enter a parse tree produced by LALGParser#formalParameter.
    def enterFormalParameter(self, ctx:LALGParser.FormalParameterContext):
        pass

    # Exit a parse tree produced by LALGParser#formalParameter.
    def exitFormalParameter(self, ctx:LALGParser.FormalParameterContext):
        pass


    # Enter a parse tree produced by LALGParser#formalParameterSection.
    def enterFormalParameterSection(self, ctx:LALGParser.FormalParameterSectionContext):
        pass

    # Exit a parse tree produced by LALGParser#formalParameterSection.
    def exitFormalParameterSection(self, ctx:LALGParser.FormalParameterSectionContext):
        pass


    # Enter a parse tree produced by LALGParser#compoundStatement.
    def enterCompoundStatement(self, ctx:LALGParser.CompoundStatementContext):
        pass

    # Exit a parse tree produced by LALGParser#compoundStatement.
    def exitCompoundStatement(self, ctx:LALGParser.CompoundStatementContext):
        pass


    # Enter a parse tree produced by LALGParser#statement.
    def enterStatement(self, ctx:LALGParser.StatementContext):
        pass

    # Exit a parse tree produced by LALGParser#statement.
    def exitStatement(self, ctx:LALGParser.StatementContext):
        pass


    # Enter a parse tree produced by LALGParser#assignmentStatement.
    def enterAssignmentStatement(self, ctx:LALGParser.AssignmentStatementContext):
        pass

    # Exit a parse tree produced by LALGParser#assignmentStatement.
    def exitAssignmentStatement(self, ctx:LALGParser.AssignmentStatementContext):
        pass


    # Enter a parse tree produced by LALGParser#procedureStatement.
    def enterProcedureStatement(self, ctx:LALGParser.ProcedureStatementContext):
        pass

    # Exit a parse tree produced by LALGParser#procedureStatement.
    def exitProcedureStatement(self, ctx:LALGParser.ProcedureStatementContext):
        pass


    # Enter a parse tree produced by LALGParser#conditionalStatement.
    def enterConditionalStatement(self, ctx:LALGParser.ConditionalStatementContext):
        pass

    # Exit a parse tree produced by LALGParser#conditionalStatement.
    def exitConditionalStatement(self, ctx:LALGParser.ConditionalStatementContext):
        pass


    # Enter a parse tree produced by LALGParser#repetetiveStatement.
    def enterRepetetiveStatement(self, ctx:LALGParser.RepetetiveStatementContext):
        pass

    # Exit a parse tree produced by LALGParser#repetetiveStatement.
    def exitRepetetiveStatement(self, ctx:LALGParser.RepetetiveStatementContext):
        pass


    # Enter a parse tree produced by LALGParser#expression.
    def enterExpression(self, ctx:LALGParser.ExpressionContext):
        pass

    # Exit a parse tree produced by LALGParser#expression.
    def exitExpression(self, ctx:LALGParser.ExpressionContext):
        pass


    # Enter a parse tree produced by LALGParser#relationalOperator.
    def enterRelationalOperator(self, ctx:LALGParser.RelationalOperatorContext):
        pass

    # Exit a parse tree produced by LALGParser#relationalOperator.
    def exitRelationalOperator(self, ctx:LALGParser.RelationalOperatorContext):
        pass


    # Enter a parse tree produced by LALGParser#simpleExpression.
    def enterSimpleExpression(self, ctx:LALGParser.SimpleExpressionContext):
        pass

    # Exit a parse tree produced by LALGParser#simpleExpression.
    def exitSimpleExpression(self, ctx:LALGParser.SimpleExpressionContext):
        pass


    # Enter a parse tree produced by LALGParser#additiveOperator.
    def enterAdditiveOperator(self, ctx:LALGParser.AdditiveOperatorContext):
        pass

    # Exit a parse tree produced by LALGParser#additiveOperator.
    def exitAdditiveOperator(self, ctx:LALGParser.AdditiveOperatorContext):
        pass


    # Enter a parse tree produced by LALGParser#term.
    def enterTerm(self, ctx:LALGParser.TermContext):
        pass

    # Exit a parse tree produced by LALGParser#term.
    def exitTerm(self, ctx:LALGParser.TermContext):
        pass


    # Enter a parse tree produced by LALGParser#multiplicativeOperator.
    def enterMultiplicativeOperator(self, ctx:LALGParser.MultiplicativeOperatorContext):
        pass

    # Exit a parse tree produced by LALGParser#multiplicativeOperator.
    def exitMultiplicativeOperator(self, ctx:LALGParser.MultiplicativeOperatorContext):
        pass


    # Enter a parse tree produced by LALGParser#factor.
    def enterFactor(self, ctx:LALGParser.FactorContext):
        pass

    # Exit a parse tree produced by LALGParser#factor.
    def exitFactor(self, ctx:LALGParser.FactorContext):
        pass


    # Enter a parse tree produced by LALGParser#unsignedNumber.
    def enterUnsignedNumber(self, ctx:LALGParser.UnsignedNumberContext):
        pass

    # Exit a parse tree produced by LALGParser#unsignedNumber.
    def exitUnsignedNumber(self, ctx:LALGParser.UnsignedNumberContext):
        pass


    # Enter a parse tree produced by LALGParser#variable.
    def enterVariable(self, ctx:LALGParser.VariableContext):
        pass

    # Exit a parse tree produced by LALGParser#variable.
    def exitVariable(self, ctx:LALGParser.VariableContext):
        pass


    # Enter a parse tree produced by LALGParser#expressionList.
    def enterExpressionList(self, ctx:LALGParser.ExpressionListContext):
        pass

    # Exit a parse tree produced by LALGParser#expressionList.
    def exitExpressionList(self, ctx:LALGParser.ExpressionListContext):
        pass


    # Enter a parse tree produced by LALGParser#identifier.
    def enterIdentifier(self, ctx:LALGParser.IdentifierContext):
        pass

    # Exit a parse tree produced by LALGParser#identifier.
    def exitIdentifier(self, ctx:LALGParser.IdentifierContext):
        pass



del LALGParser