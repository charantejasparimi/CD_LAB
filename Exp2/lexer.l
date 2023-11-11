%{
#include "y.tab.h"
%}

%%
[0-9]+              { yylval.num = atoi(yytext); return NUMBER; }
[ \t]               ;  // Ignore whitespace
[-+*/()]            { return yytext[0]; }
\n                  { return EOL; }
.                   { yyerror("Invalid character"); }

%%

int yywrap() {
    return 1;
}
