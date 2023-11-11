%{
#include <stdio.h>
%}

%token NUMBER
%token PLUS MINUS MULTIPLY DIVIDE LPAREN RPAREN EOL

%%
expression: expression PLUS term
          | expression MINUS term
          | term
          ;

term: term MULTIPLY factor
    | term DIVIDE factor
    | factor
    ;

factor: NUMBER
      | LPAREN expression RPAREN
      ;

%%

int main() {
    yyparse();
    return 0;
}

void yyerror(const char* s) {
    fprintf(stderr, "Error: %s\n", s);
}

int yywrap() {
    return 1;
}
