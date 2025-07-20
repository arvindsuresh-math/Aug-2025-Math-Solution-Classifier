def solve():
    """Index: 4263.
    Returns: the total amount John got from his grandparents.
    """
    # L1
    grandpa_money = 30 # John gets $30 from his grandpa
    grandma_multiplier = 3 # 3 times that much from his grandma
    grandma_money = grandpa_money * grandma_multiplier

    # L2
    total_money = grandpa_money + grandma_money

    # FA
    answer = total_money
    return answer