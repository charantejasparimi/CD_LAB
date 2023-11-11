def compute_leading_and_trailing_sets(grammar):
    first_sets = compute_first_sets(grammar)
    follow_sets = compute_follow_sets(grammar, first_sets)

    leading_sets = {}
    trailing_sets = {}

    for nonterminal in grammar:
        compute_leading_recursive(grammar, nonterminal, first_sets, leading_sets)
        compute_trailing_recursive(grammar, nonterminal, follow_sets, trailing_sets)

    return leading_sets, trailing_sets

def compute_first_sets(grammar):
    first_sets = {}

    for nonterminal in grammar:
        compute_first_recursive(grammar, nonterminal, first_sets)

    return first_sets

def compute_first_recursive(grammar, symbol, first_sets):
    if symbol in first_sets:
        return first_sets[symbol]

    productions = grammar[symbol]

    for production in productions:
        for i, symbol in enumerate(production):
            if symbol.isupper():
                first_set = compute_first_recursive(grammar, symbol, first_sets)
                first_sets[symbol] = first_sets.get(symbol, set()).union(first_set - {'e'})
                if 'e' not in first_set:
                    break
            else:
                first_sets[symbol] = first_sets.get(symbol, set()).union({symbol})
                break
    return first_sets[symbol]

def compute_follow_sets(grammar, first_sets):
    follow_sets = {}

    for nonterminal in grammar:
        follow_sets[nonterminal] = set()

    follow_sets[list(grammar.keys())[0]].add('$')

    for nonterminal in grammar:
        compute_follow_recursive(grammar, nonterminal, first_sets, follow_sets)

    return follow_sets

def compute_follow_recursive(grammar, symbol, first_sets, follow_sets):
    for nonterminal, productions in grammar.items():
        for production in productions:
            for i, current_symbol in enumerate(production):
                if current_symbol == symbol:
                    if i < len(production) - 1:
                        next_symbol = production[i + 1]
                        if next_symbol.isupper():
                            follow_set = compute_first_recursive(grammar, next_symbol, first_sets)
                            follow_sets[symbol] = follow_sets.get(symbol, set()).union(follow_set - {'e'})
                            if 'e' in follow_set:
                                follow_sets[symbol] = follow_sets.get(symbol, set()).union(compute_follow_sets(grammar, first_sets)[nonterminal])
                        else:
                            follow_sets[symbol] = follow_sets.get(symbol, set()).union({next_symbol})
                    elif nonterminal != symbol:
                        follow_sets[symbol] = follow_sets.get(symbol, set()).union(compute_follow_sets(grammar, first_sets)[nonterminal])
    return follow_sets[symbol]

def compute_leading_recursive(grammar, symbol, first_sets, leading_sets):
    if symbol in leading_sets:
        return leading_sets[symbol]

    leading_sets[symbol] = set()

    for nonterminal, productions in grammar.items():
        for production in productions:
            if production[0] == symbol:
                if production[1] and production[1].isupper():
                    leading_set = compute_leading_recursive(grammar, production[1], first_sets, leading_sets)
                    leading_sets[symbol] = leading_sets.get(symbol, set()).union(leading_set - {'e'})
                    if 'e' in leading_set:
                        leading_sets[symbol] = leading_sets.get(symbol, set()).union(compute_leading_recursive(grammar, nonterminal, first_sets, leading_sets))

    return leading_sets[symbol]

def compute_trailing_recursive(grammar, symbol, follow_sets, trailing_sets):
    if symbol in trailing_sets:
        return trailing_sets[symbol]

    trailing_sets[symbol] = set()

    for nonterminal, productions in grammar.items():
        for production in productions:
            if production[-1] == symbol:
                if production[-2] and production[-2].isupper():
                    trailing_set = compute_trailing_recursive(grammar, production[-2], follow_sets, trailing_sets)
                    trailing_sets[symbol] = trailing_sets.get(symbol, set()).union(trailing_set - {'e'})
                    if 'e' in trailing_set:
                        trailing_sets[symbol] = trailing_sets.get(symbol, set()).union(compute_trailing_recursive(grammar, nonterminal, follow_sets, trailing_sets))

    return trailing_sets[symbol]

if __name__ == '__main__':
    example_grammar = {
        'S': ['AB', 'BC'],
        'A': ['aA', ''],
        'B': ['bB', ''],
        'C': ['cC', '']
    }

    leading_sets, trailing_sets = compute_leading_and_trailing_sets(example_grammar)

    print("Leading Sets:")
    for nonterminal, leading_set in leading_sets.items():
        print(f"{nonterminal}: {leading_set}")

    print("\nTrailing Sets:")
    for nonterminal, trailing_set in trailing_sets.items():
        print(f"{nonterminal}: {trailing_set}")
