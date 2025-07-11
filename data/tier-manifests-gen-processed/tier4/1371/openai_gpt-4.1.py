def solve():
    """Index: 1371.
    Returns: the amount of money Lucy gets.
    """
    # L1
    total_money = 10000 # $10,000 to split up between his kids
    natalie_divisor = 2 # Natalie will get half
    natalie_share = total_money / natalie_divisor

    # L2
    money_after_natalie = total_money - natalie_share

    # L3
    rick_percent = 0.60 # Rick will get 60 percent of the remaining money
    rick_share = money_after_natalie * rick_percent

    # L4
    lucy_share = money_after_natalie - rick_share

    # FA
    answer = lucy_share
    return answer