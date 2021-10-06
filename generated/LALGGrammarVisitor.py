# Generated from LALGGrammar.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LALGGrammarParser import LALGGrammarParser
else:
    from LALGGrammarParser import LALGGrammarParser

# This class defines a complete generic visitor for a parse tree produced by LALGGrammarParser.

class LALGGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LALGGrammarParser#programa.
    def visitPrograma(self, ctx:LALGGrammarParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LALGGrammarParser#bloco.
    def visitBloco(self, ctx:LALGGrammarParser.BlocoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LALGGrammarParser#parteDeclaracaoVariaveis.
    def visitParteDeclaracaoVariaveis(self, ctx:LALGGrammarParser.ParteDeclaracaoVariaveisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LALGGrammarParser#declaracaoVariaveis.
    def visitDeclaracaoVariaveis(self, ctx:LALGGrammarParser.DeclaracaoVariaveisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LALGGrammarParser#tipoSimples.
    def visitTipoSimples(self, ctx:LALGGrammarParser.TipoSimplesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LALGGrammarParser#listaIdentificadores.
    def visitListaIdentificadores(self, ctx:LALGGrammarParser.ListaIdentificadoresContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LALGGrammarParser#parteDeclaracaoSubRotinas.
    def visitParteDeclaracaoSubRotinas(self, ctx:LALGGrammarParser.ParteDeclaracaoSubRotinasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LALGGrammarParser#declaracaoProcedimento.
    def visitDeclaracaoProcedimento(self, ctx:LALGGrammarParser.DeclaracaoProcedimentoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LALGGrammarParser#parametrosFormais.
    def visitParametrosFormais(self, ctx:LALGGrammarParser.ParametrosFormaisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LALGGrammarParser#secaoParametrosFormais.
    def visitSecaoParametrosFormais(self, ctx:LALGGrammarParser.SecaoParametrosFormaisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LALGGrammarParser#comandoComposto.
    def visitComandoComposto(self, ctx:LALGGrammarParser.ComandoCompostoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LALGGrammarParser#comando.
    def visitComando(self, ctx:LALGGrammarParser.ComandoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LALGGrammarParser#atribuicao.
    def visitAtribuicao(self, ctx:LALGGrammarParser.AtribuicaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LALGGrammarParser#chamadaProcedimento.
    def visitChamadaProcedimento(self, ctx:LALGGrammarParser.ChamadaProcedimentoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LALGGrammarParser#comandoCondicional.
    def visitComandoCondicional(self, ctx:LALGGrammarParser.ComandoCondicionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LALGGrammarParser#comandoRepetitivo.
    def visitComandoRepetitivo(self, ctx:LALGGrammarParser.ComandoRepetitivoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LALGGrammarParser#expressao.
    def visitExpressao(self, ctx:LALGGrammarParser.ExpressaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LALGGrammarParser#expressaoSimples.
    def visitExpressaoSimples(self, ctx:LALGGrammarParser.ExpressaoSimplesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LALGGrammarParser#termo.
    def visitTermo(self, ctx:LALGGrammarParser.TermoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LALGGrammarParser#fator.
    def visitFator(self, ctx:LALGGrammarParser.FatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LALGGrammarParser#variavel.
    def visitVariavel(self, ctx:LALGGrammarParser.VariavelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LALGGrammarParser#listaExpressoes.
    def visitListaExpressoes(self, ctx:LALGGrammarParser.ListaExpressoesContext):
        return self.visitChildren(ctx)



del LALGGrammarParser