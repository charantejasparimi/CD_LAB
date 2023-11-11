def generate_predictive_parse_table(grammar, first_sets, follow_sets):
    table = {}

    for nonterminal, productions in grammar.items():
        for production in productions:
            first_set = compute_first_of_string(production, first_sets)
            for terminal in first_set:
                if terminal != 'e':
                    table[(nonterminal, terminal)] = production

            if 'e' in first_set:
                follow_set = follow_sets[nonterminal]
                for terminal in follow_set:
                    if (nonterminal, terminal) not in table:
                        table[(nonterminal, terminal)] = production

    return table

def compute_first_of_string(string, first_sets):
    first_set = set()

    for symbol in string:
        if symbol.isupper():
            first_set = first_set.union(first_sets[symbol] - {'e'})
            if 'e' not in first_sets[symbol]:
                break
        else:
            first_set.add(symbol)
            break

    return first_set

if __name__ == '__main__':
    example_grammar = {
        'S': ['E$'],
        'E': ['TQ'],
        'Q': ['+TQ', 'e'],
        'T': ['FR'],
        'R': ['*FR', 'e'],
        'F': ['(E)', 'id']
    }

    first_sets = {
        'S': {'(', 'id'},
        'E': {'(', 'id'},
        'Q': {'+', 'e'},
        'T': {'(', 'id'},
        'R': {'*', 'e'},
        'F': {'(', 'id'}
    }

    follow_sets = {
        'S': {'$', ')'},
        'E': {'$', ')', '+'},
        'Q': {'$', ')'},
        'T': {'$', ')', '+', '*'},
        'R': {'$', ')', '+'},
        'F': {'$', ')', '+', '*'}
    }

    parse_table = generate_predictive_parse_table(example_grammar, first_sets, follow_sets)

    print("Predictive Parse Table:")
    for key, production in parse_table.items():
        print(f"{key}: {production}")
