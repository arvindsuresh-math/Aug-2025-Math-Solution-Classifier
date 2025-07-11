def solve():
    """Index: 711.
    Returns: the number of oranges Alice sold.
    """
    # L1
    total_oranges = 180 # In total, they sold 180 oranges
    parts = 3 # Alice sold twice as many oranges as Emily did (Emily 1 part, Alice 2 parts, total 3 parts)
    emily_oranges = total_oranges / parts

    # L2
    alice_multiplier = 2 # Alice sold twice as many oranges as Emily did
    alice_oranges = emily_oranges * alice_multiplier

    # FA
    answer = alice_oranges
    return answer