def solve():
    """Index: 5900.
    Returns: the number of coconut trees Alvin has to harvest.
    """
    # L1
    money_needed = 90 # Alvin needs $90
    price_per_coconut = 3 # a coconut can be sold for $3
    coconuts_needed = money_needed / price_per_coconut

    # L2
    coconuts_per_tree = 5 # coconut trees that yield 5 coconuts each
    trees_to_harvest = coconuts_needed / coconuts_per_tree

    # FA
    answer = trees_to_harvest
    return answer