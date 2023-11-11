%{
#include <stdio.h>
%}

%token NUMBER
%token PLUS MINUS MULTIPLY DIVIDE LPAREN RPAREN EOL

%%
expression: expression PLUS term   { $$ = $1 + $3; }
          | expression MINUS term  { $$ = $1 - $3; }
          | term                  { $$ = $1; }
          ;

term: term MULTIPLY factor       { $$ = $1 * $3; }
    | term DIVIDE factor         { $$ = $1 / $3; }
    | factor                    { $$ = $1; }
    ;

factor: NUMBER                   { $$ = $1; }
      | LPAREN expression RPAREN { $$ = $2; }
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
