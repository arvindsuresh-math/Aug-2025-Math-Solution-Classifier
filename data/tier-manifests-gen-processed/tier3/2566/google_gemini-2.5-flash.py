def solve():
    """Index: 2566.
    Returns: the total amount of money Madeline and her brother have together.
    """
    # L1
    madeline_money = 48 # Madeline has $48
    half_divisor = 2 # her brother has half as much
    brother_money = madeline_money / half_divisor

    # L2
    total_money = madeline_money + brother_money

    # FA
    answer = total_money
    return answer