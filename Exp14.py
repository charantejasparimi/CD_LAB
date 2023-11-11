def calculate_closure(productions, closure):
    new_items_added = True

    while new_items_added:
        new_items_added = False

        for item in closure.copy():
            dot_index = item.index('.')
            if dot_index < len(item) - 1 and item[dot_index + 1].isupper():
                next_symbol = item[dot_index + 1]
                for production in productions[next_symbol]:
                    new_item = '.' + production
                    if new_item not in closure:
                        closure.add(new_item)
                        new_items_added = True

    return closure

def calculate_goto(closure, symbol, productions):
    new_items = set()

    for item in closure:
        dot_index = item.index('.')
        if dot_index < len(item) - 1 and item[dot_index + 1] == symbol:
            new_item = item[:dot_index] + symbol + '.' + item[dot_index + 2:]
            new_items.add(new_item)

    return calculate_closure(productions, new_items)

def calculate_lr0_items(grammar):
    productions = grammar['productions']
    start_symbol = grammar['start_symbol']

    initial_item = '.' + productions[start_symbol][0]
    initial_closure = calculate_closure(productions, {initial_item})

    items = [initial_closure]

    for item in items:
        for symbol in grammar['terminals'] + grammar['nonterminals']:
            goto_set = calculate_goto(item, symbol, productions)
            if goto_set and goto_set not in items:
                items.append(goto_set)

    return items

if __name__ == '__main__':
    example_grammar = {
        'productions': {
            'S': ['E'],
            'E': ['E+T', 'T'],
            'T': ['T*F', 'F'],
            'F': ['(E)', 'id']
        },
        'terminals': ['+', '*', '(', ')', 'id'],
        'nonterminals': ['S', 'E', 'T', 'F'],
        'start_symbol': 'S'
    }

    lr0_items = calculate_lr0_items(example_grammar)

    print("LR(0) Items:")
    for i, item_set in enumerate(lr0_items):
        print(f"I{i}: {', '.join(sorted(item_set))}")
