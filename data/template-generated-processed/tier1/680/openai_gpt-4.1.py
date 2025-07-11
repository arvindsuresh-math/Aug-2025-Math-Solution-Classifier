def solve():
    """Index: 680.
    Returns: the total amount of money Cecil, Catherine, and Carmela have altogether.
    """
    # L1
    cecil_money = 600 # Cecil has $600
    twice_cecil = cecil_money * 2

    # L2
    catherine_less = 250 # Catherine has $250 less than twice as much as Cecil
    catherine_money = twice_cecil - catherine_less

    # L3
    carmela_more = 50 # Carmela has $50 more than twice Cecil's money
    carmela_money = twice_cecil + carmela_more

    # L4
    total_money = cecil_money + catherine_money + carmela_money

    # FA
    answer = total_money
    return answer