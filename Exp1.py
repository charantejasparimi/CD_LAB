import re

class Token:
    def __init__(self, token_type, value):
        self.token_type = token_type
        self.value = value

class Tokenizer:
    def __init__(self, source_code):
        self.source_code = source_code
        self.tokens = []
        self.current_pos = 0

    def tokenize(self):
        while self.current_pos < len(self.source_code):
            if self.match(r'\d+'):
                self.add_token('NUMBER', int(self.matched_text))
            elif self.match(r'\w+'):
                self.add_token('IDENTIFIER', self.matched_text)
            elif self.match(r'\+'):
                self.add_token('PLUS', '+')
            elif self.match(r'\-'):
                self.add_token('MINUS', '-')
            elif self.match(r'\*'):
                self.add_token('MULTIPLY', '*')
            elif self.match(r'\/'):
                self.add_token('DIVIDE', '/')
            elif self.match(r'\('):
                self.add_token('LPAREN', '(')
            elif self.match(r'\)'):
                self.add_token('RPAREN', ')')
            elif self.match(r'\s+'):
                pass  # Ignore whitespace
            else:
                self.add_token('UNKNOWN', self.source_code[self.current_pos])
                self.current_pos += 1

    def add_token(self, token_type, value):
        self.tokens.append(Token(token_type, value))

    def match(self, pattern):
        match = re.match(pattern, self.source_code[self.current_pos:])
        if match:
            self.matched_text = match.group()
            self.current_pos += len(self.matched_text)
            return True
        return False

if __name__ == '__main__':
    source_code = "2 + 3 * (4 - 1)"
    tokenizer = Tokenizer(source_code)
    tokenizer.tokenize()
    for token in tokenizer.tokens:
        print(f"{token.token_type}: {token.value}")
