grammar LALGGrammar;

PALAVRA_RES: 'procedure' | 'begin' | 'end' | 'if' | 'then' | 'else' | 'while' | 'do' ;

VARIAVEL: 'var' ;

PROGRAMA: 'program' ;

OP_LOG: 'and' | 'or' | 'not' ;

OP_ARIT: '+' | '-' | 'div' | '*' ;

ABREPARENT: '(' ;

FECHAPARENT: ')' ;

PONTO: ';' | '.' | ',' | ':' ;

TIPO_SIMPLES: 'int' | 'real' | 'boolean' ;

ATRIBUICAO: ':=' ;

NUMINT: ('0'..'9')+ ;

NUMREAL: ('0'..'9')+ ('.' ('0'..'9')+)? ;


fragment

OP_REL: '>' | '>=' | '<' | '<=' | '<>' | '=' ;

ENT_SAIDA: 'read' | 'write' ;

IDENTIFICADOR: ('a'..'z' | 'A'..'Z' | '_') ('a'..'z' | 'A'..'Z' | '_' | '0'..'9')* ;

COMENTARIO_COM_BARRA: ('//' ~('\n' | '\r')* '\r'? '\n') -> skip ;

COMENTARIO_COM_PARENTESES: '{' ~('}' | '{')* '}' ;

WS: ( ' ' | '\t' | '\r' | '\n') -> skip ;


programa: 'program' IDENTIFICADOR ';' bloco EOF ;


bloco: (parteDeclaracaoVariaveis parteDeclaracaoSubRotinas comandoComposto) | (parteDeclaracaoVariaveis comandoComposto) | (parteDeclaracaoSubRotinas comandoComposto) | (comandoComposto) ; 

parteDeclaracaoVariaveis: declaracaoVariaveis (';' declaracaoVariaveis)* ';' ; 

declaracaoVariaveis: tipoSimples listaIdentificadores ;

tipoSimples: TIPO_SIMPLES ;

listaIdentificadores: IDENTIFICADOR (',' IDENTIFICADOR)* ;

parteDeclaracaoSubRotinas: (declaracaoProcedimento';')* ;

declaracaoProcedimento: ('procedure' IDENTIFICADOR parametrosFormais ';' bloco) | ('procedure' IDENTIFICADOR';' bloco) ;

parametrosFormais: '(' secaoParametrosFormais (';' secaoParametrosFormais)* ')' ;

secaoParametrosFormais: ('var' listaIdentificadores ':' IDENTIFICADOR) | (listaIdentificadores ':' IDENTIFICADOR) ;

comandoComposto: 'begin' comando (';' comando)* 'end' ;

comando: (atribuicao | chamadaProcedimento | comandoComposto | comandoCondicional | comandoRepetitivo) ;

atribuicao: variavel ':=' expressao ;

chamadaProcedimento: IDENTIFICADOR '(' listaExpressoes ')' | IDENTIFICADOR ;

comandoCondicional: ('if' expressao 'then' comando 'else' comando) | ('if' expressao 'then' comando) ;

comandoRepetitivo: 'while' expressao 'do' comando ; 


expressao: (expressaoSimples) | (expressaoSimples OP_REL expressaoSimples);

expressaoSimples: (('+' | '-') termo (('+' | '-' | 'or') termo)*) | (termo (('+' | '-' | 'or') termo)*) ;

termo: fator (('*' | 'div' | 'and') fator)* ;

fator: (variavel | NUMINT | '(' expressao ')' | 'not' fator) ;

variavel: IDENTIFICADOR | IDENTIFICADOR (expressao);

listaExpressoes : expressao (',' expressao)* ;