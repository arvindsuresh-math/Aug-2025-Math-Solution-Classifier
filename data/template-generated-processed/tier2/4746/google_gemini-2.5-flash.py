def solve():
    """Index: 4746.
    Returns: the total number of broken marbles.
    """
    # L1
    first_set_total_marbles = 50 # The first set contains 50 marbles
    first_set_broken_percent_decimal = 0.1 # 10% of her marbles are broken
    first_set_broken_marbles = first_set_total_marbles * first_set_broken_percent_decimal

    # L2
    second_set_total_marbles = 60 # The second set contains 60
    second_set_broken_percent_decimal = 0.2 # 20% of the marbles are broken
    second_set_broken_marbles = second_set_total_marbles * second_set_broken_percent_decimal

    # L3
    total_broken_marbles = first_set_broken_marbles + second_set_broken_marbles

    # FA
    answer = total_broken_marbles
    return answer