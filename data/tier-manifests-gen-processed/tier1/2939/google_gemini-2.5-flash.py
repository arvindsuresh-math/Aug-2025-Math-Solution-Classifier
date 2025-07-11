def solve():
    """Index: 2939.
    Returns: the number of more pebbles Lance threw compared to Candy.
    """
    # L1
    candy_pebbles = 4 # 4 pebbles
    lance_multiplier = 3 # 3 times as many pebbles as Candy
    lance_pebbles = candy_pebbles * lance_multiplier

    # L2
    more_pebbles_lance_than_candy = lance_pebbles - candy_pebbles

    # FA
    answer = more_pebbles_lance_than_candy
    return answer