grammar PythonToJava;

// Reglas principales
program : (statement | function)* EOF;
statement : assignment | printStmt | returnStmt | functionCall;
function : DEF ID LPAREN parameters? RPAREN COLON NEWLINE INDENT (statement | returnStmt)+ DEDENT;
assignment : ID ASSIGN expression NEWLINE;
printStmt : PRINT LPAREN expression RPAREN NEWLINE;
returnStmt : RETURN expression NEWLINE;
functionCall : ID LPAREN arguments? RPAREN;

// Parámetros y argumentos
parameters : ID (COMMA ID)*;
arguments : expression (COMMA expression)*;

// Expresiones
expression : atom (op atom)*;
atom : ID | NUMBER | STRING | functionCall;
op : PLUS | MINUS | MUL | DIV;

// Tokens
DEF     : 'def';
RETURN  : 'return';
PRINT   : 'print';
IF      : 'if';
ELSE    : 'else';
FOR     : 'for';
IN      : 'in';
COLON   : ':';
LPAREN  : '(';
RPAREN  : ')';
LBRACE  : '{';
RBRACE  : '}';
COMMA   : ',';
ASSIGN  : '=';
PLUS    : '+';
MINUS   : '-';
DIV     : '/';
MUL     : '*';
ID      : [a-zA-Z_][a-zA-Z_0-9]*;
NUMBER  : [0-9]+;
STRING  : '"' .*? '"';
NEWLINE : '\r'? '\n';
WS      : [ \t]+ -> skip;
