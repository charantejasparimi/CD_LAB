def eliminate_left_factoring(grammar):
    new_grammar = {}

    for nonterminal, productions in grammar.items():
        common_prefixes = find_common_prefixes(productions)

        if common_prefixes:
            new_nonterminal = nonterminal + "'"
            new_grammar[nonterminal] = [prefix + new_nonterminal for prefix in common_prefixes]
            new_grammar[new_nonterminal] = [production[len(prefix):] or 'e' for prefix in common_prefixes]

        else:
            new_grammar[nonterminal] = productions

    return new_grammar

def find_common_prefixes(productions):
    common_prefixes = []
    prefix = ""

    while all(production.startswith(prefix) for production in productions):
        common_prefixes.append(prefix)
        if not productions:
            break
        prefix += productions[0][len(prefix)]

    return common_prefixes

if __name__ == '__main__':
    original_grammar = {
        'S': ['abc', 'abd', 'axyz', 'aef'],
        'A': ['abc', 'axyz', 'aef'],
    }

    updated_grammar = eliminate_left_factoring(original_grammar)

    print("Original Grammar:")
    for nonterminal, productions in original_grammar.items():
        print(f"{nonterminal} -> {' | '.join(productions)}")

    print("\nGrammar after Left Factoring Elimination:")
    for nonterminal, productions in updated_grammar.items():
        print(f"{nonterminal} -> {' | '.join(productions)}")
