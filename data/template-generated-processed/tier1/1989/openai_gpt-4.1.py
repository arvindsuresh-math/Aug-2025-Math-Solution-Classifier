def solve():
    """Index: 1989.
    Returns: the amount Yulia spent to operate her lemonade stand, in dollars.
    """
    # L1
    lemonade_gross = 47 # lemonade stand made a gross revenue of $47
    babysit_income = 31 # made $31 babysitting
    total_gross = lemonade_gross + babysit_income

    # L2
    profit = 44 # net $44 in profit
    overhead = total_gross - profit

    # FA
    answer = overhead
    return answer