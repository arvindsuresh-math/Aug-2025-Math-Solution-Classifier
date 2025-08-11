def solve():
    """Index: 680.
    Returns: the total amount of money they have altogether.
    """
    # L1
    cecil_money = 600 # Cecil has $600
    multiplier_twice = 2 # twice as much
    twice_cecil_money = cecil_money * multiplier_twice

    # L2
    catherine_less_than_twice = 250 # $250 less than twice as much as Cecil
    catherine_money = twice_cecil_money - catherine_less_than_twice

    # L3
    carmela_more_than_twice = 50 # $50 more than twice Cecil's money
    carmela_money = twice_cecil_money + carmela_more_than_twice

    # L4
    total_money = cecil_money + catherine_money + carmela_money

    # FA
    answer = total_money
    return answer