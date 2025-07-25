def solve():
    """Index: 2690.
    Returns: the number of apples Samuel has left.
    """
    # L1
    more_apples_than_bonnie = 20 # Samuel bought 20 more apples than Bonnie
    bonnie_apples = 8 # Bonnie bought 8 apples
    samuel_bought_apples = more_apples_than_bonnie + bonnie_apples

    # L2
    ate_divisor = 2 # Samuel then ate half of them
    samuel_ate_apples = samuel_bought_apples / ate_divisor

    # L3
    pie_divisor = 7 # used 1/7 of them to make apple pie
    samuel_used_for_pie = samuel_bought_apples / pie_divisor

    # L4
    samuel_apples_left = samuel_bought_apples - samuel_ate_apples - samuel_used_for_pie

    # FA
    answer = samuel_apples_left
    return answer