def solve():
    """Index: 2939.
    Returns: how many more pebbles Lance threw compared to Candy.
    """
    # L1
    candy_pebbles = 4 # Candy throws 4 pebbles
    lance_multiplier = 3 # 3 times as many pebbles as Candy
    lance_pebbles = candy_pebbles * lance_multiplier

    # L2
    pebbles_more = lance_pebbles - candy_pebbles

    # FA
    answer = pebbles_more
    return answer