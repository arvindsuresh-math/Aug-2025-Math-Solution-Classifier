def solve():
    """Index: 6495.
    Returns: the number of trees Bart needs to cut down.
    """
    # L1
    days_in_november = 30 # WK
    days_in_december = 31 # WK
    days_in_january = 31 # WK
    days_in_february = 28 # WK
    total_days = days_in_november + days_in_december + days_in_january + days_in_february

    # L2
    burn_rate_per_day = 5 # burns 5 logs a day
    total_pieces_burned = total_days * burn_rate_per_day

    # L3
    pieces_per_tree = 75 # 75 pieces of firewood
    trees_needed = total_pieces_burned / pieces_per_tree

    # FA
    answer = trees_needed
    return answer