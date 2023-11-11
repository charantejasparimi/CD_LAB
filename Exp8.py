from collections import defaultdict

def compute_first(grammar):
    first = defaultdict(set)
    epsilon = 'e'

    for nonterminal in grammar:
        compute_first_recursive(grammar, nonterminal, first)

    return first

def compute_first_recursive(grammar, symbol, first):
    if symbol in first:
        return first[symbol]

    productions = grammar[symbol]

    for production in productions:
        for i, symbol in enumerate(production):
            if symbol.isupper():
                first_set = compute_first_recursive(grammar, symbol, first)
                first[symbol].update(first_set - {epsilon})
                if epsilon not in first_set:
                    break
            else:
                first[symbol].add(symbol)
                break
    return first[symbol]

def compute_follow(grammar, first):
    follow = defaultdict(set)
    start_symbol = list(grammar.keys())[0]
    follow[start_symbol].add('$')

    for nonterminal in grammar:
        compute_follow_recursive(grammar, nonterminal, first, follow)

    return follow

def compute_follow_recursive(grammar, symbol, first, follow):
    for nonterminal, productions in grammar.items():
        for production in productions:
            for i, current_symbol in enumerate(production):
                if current_symbol == symbol:
                    if i < len(production) - 1:
                        next_symbol = production[i + 1]
                        if next_symbol.isupper():
                            follow_set = compute_first_recursive(grammar, next_symbol, first)
                            follow[symbol].update(follow_set - {epsilon})
                            if epsilon in follow_set:
                                follow[symbol].update(compute_follow_recursive(grammar, nonterminal, first, follow))
                        else:
                            follow[symbol].add(next_symbol)
                    elif nonterminal != symbol:
                        follow[symbol].update(compute_follow_recursive(grammar, nonterminal, first, follow))
    return follow[symbol]

if __name__ == '__main__':
    grammar = {
        'S': ['AaB', 'BbAc'],
        'A': ['Ba', 'e'],
        'B': ['Ab', 'e'],
    }

    first_sets = compute_first(grammar)
    follow_sets = compute_follow(grammar, first_sets)

    print("First sets:")
    for nonterminal, first_set in first_sets.items():
        print(f"{nonterminal}: {first_set}")

    print("\nFollow sets:")
    for nonterminal, follow_set in follow_sets.items():
        print(f"{nonterminal}: {follow_set}")
