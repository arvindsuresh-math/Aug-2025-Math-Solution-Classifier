def solve():
    """Index: 5874.
    Returns: the total number of frogs in both ponds combined.
    """
    # L1
    frogs_pond_a = 32 # 32 frogs in Pond A
    divisor_for_pond_b = 2 # twice as many frogs as Pond B
    frogs_pond_b = frogs_pond_a / divisor_for_pond_b

    # L2
    total_frogs = frogs_pond_a + frogs_pond_b

    # FA
    answer = total_frogs
    return answer