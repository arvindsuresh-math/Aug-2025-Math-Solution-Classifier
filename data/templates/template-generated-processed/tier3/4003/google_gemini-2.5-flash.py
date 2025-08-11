def solve():
    """Index: 4003.
    Returns: the total money the three of them have.
    """
    joanna_money = 8 # Joanna has $8

    # L2
    brother_multiplier = 3 # her brother has thrice as much
    brother_money = joanna_money * brother_multiplier

    # L3
    sister_divisor = 2 # her sister has only half as much
    sister_money = joanna_money / sister_divisor

    # L4
    total_money = joanna_money + brother_money + sister_money

    # FA
    answer = total_money
    return answer