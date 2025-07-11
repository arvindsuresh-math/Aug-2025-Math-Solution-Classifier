def solve():
    """Index: 788.
    Returns: how much more money Christopher has than Karen.
    """
    # L1
    christopher_quarters = 64 # Christopher has 64 quarters
    quarter_value = 0.25 # WK: value of a quarter
    christopher_money = christopher_quarters * quarter_value

    # L2
    karen_quarters = 32 # Karen has 32 quarters
    karen_money = karen_quarters * quarter_value

    # L3
    difference = christopher_money - karen_money

    # FA
    answer = difference
    return answer