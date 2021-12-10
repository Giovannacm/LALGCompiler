grammar LALG;


program: PROGRAM identifier SEMI block DOT ;

block: (variableDeclarationPart procedureDeclarationPart compoundStatement) | (compoundStatement) ; 


variableDeclarationPart: variableDeclaration (SEMI variableDeclaration)* SEMI ; 

variableDeclaration: simpleType identifierList ;

simpleType: BOOLEAN | INTEGER | REAL ;

identifierList: identifier (COMMA identifier)* ;

procedureDeclarationPart: (procedureDeclaration SEMI)* ;

procedureDeclaration: PROCEDURE identifier (formalParameter)? SEMI block ;

formalParameter: LPAREN formalParameterSection (SEMI formalParameterSection)* RPAREN ;

formalParameterSection: (VAR identifierList COLON simpleType) ;


compoundStatement: BEGIN statement (SEMI statement)* END ;

statement: (assignmentStatement | procedureStatement | compoundStatement | conditionalStatement | repetetiveStatement) ;

assignmentStatement: variable ASSIGN expression ;

procedureStatement: identifier (LPAREN expressionList RPAREN)? ;

conditionalStatement: (IF expression statement ELSE statement) | (IF expression statement) ;

repetetiveStatement: WHILE expression statement ; 


expression: simpleExpression (relationalOperator simpleExpression)? | TRUE | FALSE ;

relationalOperator: GT | GE | LT | LE | NOT_EQUAL | EQUAL ;

simpleExpression: (('+' | '-') term (additiveOperator term)*) | (term (additiveOperator term)*) ;

additiveOperator: PLUS | MINUS | OR ;

term: factor (multiplicativeOperator factor)* ;

multiplicativeOperator: STAR | DIV | AND ;

factor: variable | unsignedNumber | LPAREN expression RPAREN | NOT factor ;

unsignedNumber: NUMINT | NUMREAL ;

variable: identifier | identifier (expression);

expressionList: expression (COMMA expression)* ;

identifier: IDENT ;


BARCOMMENT: '//' .*? '\n' -> skip;

BRACKETCOMMENT: '{' .*? '}' -> skip;


PROGRAM: 'program' ;

PROCEDURE: 'procedure' ;

BEGIN: 'begin'; 

END: 'end' ;

VAR: 'var' ;

IF: 'if' ;

ELSE: 'else' ;

WHILE: 'while' ;

DO: 'do' ;

COLON: ':' ;

SEMI: ';' ;

DOT: '.' ;

COMMA: ',' ;

ASSIGN: ':=' ;

NOT: 'not' ;

LPAREN : '(' ;

RPAREN: ')' ;

BOOLEAN: 'boolean' ;

INTEGER: 'int' ;

REAL: 'real' ;

EQUAL: '=' ;

NOT_EQUAL: '<>' ;

LT: '<' ;

LE: '<=' ;

GT: '>' ;

GE: '>=' ;

PLUS: '+' ;

MINUS: '-' ;

OR: 'or' ;

STAR: '*' ;

DIV: 'div' ;

AND: 'and' ;

TRUE: 'true' ;

FALSE: 'false' ;

NUMINT: ('0'..'9')+ ;

NUMREAL: ('0'..'9')+ ('.' ('0'..'9')+)? ;

IDENT: ('a'..'z' | 'A'..'Z' | '_') ('a'..'z' | 'A'..'Z' | '_' | '0'..'9')* ;

WS: [ \t\r\n] -> skip ;