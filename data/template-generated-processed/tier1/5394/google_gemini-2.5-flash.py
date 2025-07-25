def solve():
    """Index: 5394.
    Returns: the total number of dolls Hannah and her sister have.
    """
    # L1
    hannah_multiplier = 5 # 5 times as many dolls
    sister_dolls = 8 # Her sister has 8 dolls
    hannah_dolls = hannah_multiplier * sister_dolls

    # L2
    total_dolls = sister_dolls + hannah_dolls

    # FA
    answer = total_dolls
    return answer