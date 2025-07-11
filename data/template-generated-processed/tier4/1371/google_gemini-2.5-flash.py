def solve():
    """Index: 1371.
    Returns: the amount of money Lucy gets.
    """
    # L1
    total_saved_money = 10000 # $10,000 to split up
    natalie_share_divisor = 2 # Natalie will get half
    natalie_money = total_saved_money / natalie_share_divisor

    # L2
    remaining_after_natalie = total_saved_money - natalie_money

    # L3
    rick_share_percent = 0.60 # 60 percent of the remaining money
    rick_money = remaining_after_natalie * rick_share_percent

    # L4
    lucy_money = remaining_after_natalie - rick_money

    # FA
    answer = lucy_money
    return answer