def solve():
    """Index: 1989.
    Returns: the amount Yulia spent to operate her lemonade stand.
    """
    # L1
    lemonade_revenue = 47 # gross revenue of $47 this week
    babysitting_income = 31 # made $31
    total_gross_revenue = lemonade_revenue + babysitting_income

    # L2
    profit = 44 # net $44 in profit this week
    overhead = total_gross_revenue - profit

    # FA
    answer = overhead
    return answer