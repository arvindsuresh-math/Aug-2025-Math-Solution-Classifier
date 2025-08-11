def solve():
    """Index: 7227.
    Returns: the number of pencils Elizabeth can buy.
    """
    # L1
    num_pens = 6 # 6 pens
    cost_per_pen = 2 # 2 dollars
    cost_of_pens = num_pens * cost_per_pen

    # L2
    initial_money = 20 # 20 dollars
    money_for_pencils = initial_money - cost_of_pens

    # L3
    cost_per_pencil = 1.60 # $1.60
    num_pencils = money_for_pencils / cost_per_pencil

    # FA
    answer = num_pencils
    return answer