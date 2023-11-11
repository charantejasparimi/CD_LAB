class ShiftReduceParser:
    def __init__(self, grammar):
        self.grammar = grammar
        self.stack = []
        self.input_buffer = []

    def shift(self):
        symbol = self.input_buffer.pop(0)
        self.stack.append(symbol)

    def reduce(self):
        for production in self.grammar.values():
            if self.stack[-len(production):] == production:
                for _ in range(len(production)):
                    self.stack.pop()
                nonterminal = list(self.grammar.keys())[list(self.grammar.values()).index(production)]
                self.stack.append(nonterminal)
                return True
        return False

    def parse(self, input_string):
        self.input_buffer = list(input_string) + ['$']
        self.stack = ['$', self.grammar['S'][0][0]]  # Initializing stack with $ and the start symbol

        while self.input_buffer:
            print(f"Stack: {''.join(self.stack)}\tInput: {''.join(self.input_buffer)}")

            if self.stack[-1].isupper():  # If top of stack is a nonterminal
                if not self.reduce():
                    print("Error: Cannot reduce")
                    return False
            else:  # If top of stack is a terminal
                if self.stack[-1] == self.input_buffer[0]:
                    self.stack.pop()
                    self.shift()
                else:
                    print("Error: Mismatch between stack and input")
                    return False

        print("Parsing successful!")
        return True

if __name__ == '__main__':
    # Example grammar
    grammar = {
        'S': ['E$'],
        'E': ['E+T', 'T'],
        'T': ['T*F', 'F'],
        'F': ['(E)', 'id']
    }

    # Example input string
    input_string = "id+id*id$"

    parser = ShiftReduceParser(grammar)
    parser.parse(input_string)
