def solve():
    """Index: 6691.
    Returns: the amount of money Amanda has left.
    """
    # L1
    num_tapes = 2 # two cassette tapes
    cost_per_tape = 9 # $9 each
    cost_headphones = 25 # headphone set that costs $25
    total_spent = num_tapes * cost_per_tape + cost_headphones

    # L2
    initial_gift = 50 # $50 as a gift
    money_left = initial_gift - total_spent

    # FA
    answer = money_left
    return answer