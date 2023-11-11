def eliminate_left_recursion(grammar):
    new_grammar = {}

    for nonterminal, productions in grammar.items():
        alpha_productions = []
        beta_productions = []

        for production in productions:
            if production.startswith(nonterminal):
                alpha_productions.append(production[1:] + nonterminal + "'")
            else:
                beta_productions.append(production + nonterminal + "'")

        if alpha_productions:
            new_grammar[nonterminal] = [beta + nonterminal + "'" for beta in beta_productions]
            new_grammar[nonterminal + "'"] = [alpha + nonterminal + "'" for alpha in alpha_productions] + ['e']
        else:
            new_grammar[nonterminal] = productions

    return new_grammar

if __name__ == '__main__':
    original_grammar = {
        'E': ['E+T', 'T'],
        'T': ['T*F', 'F'],
        'F': ['(E)', 'id']
    }

    updated_grammar = eliminate_left_recursion(original_grammar)

    print("Original Grammar:")
    for nonterminal, productions in original_grammar.items():
        print(f"{nonterminal} -> {' | '.join(productions)}")

    print("\nGrammar after Left Recursion Elimination:")
    for nonterminal, productions in updated_grammar.items():
        print(f"{nonterminal} -> {' | '.join(productions)}")
