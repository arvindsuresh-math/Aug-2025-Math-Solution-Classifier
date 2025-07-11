def solve():
    """Index: 2750.
    Returns: the amount Zoe earned from pool cleaning.
    """
    # L1
    julie_multiplier = 3 # three times as often as she babysat Zachary
    zachary_earnings = 600 # made $600 babysitting Zachary
    julie_earnings = julie_multiplier * zachary_earnings

    # L2
    chloe_multiplier = 5 # 1/5 the number of times she babysat Chloe (implies Chloe's earnings are 5 times Zachary's)
    chloe_earnings = chloe_multiplier * zachary_earnings

    # L3
    total_babysitting_earnings = zachary_earnings + julie_earnings + chloe_earnings

    # L4
    total_earnings = 8000 # total of $8,000
    pool_cleaning_earnings = total_earnings - total_babysitting_earnings

    # FA
    answer = pool_cleaning_earnings
    return answer