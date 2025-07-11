def solve():
    """Index: 2302.
    Returns: the price of the TV in 2009.
    """
    # L1
    year_end = 2009 # 2009
    year_start = 2001 # 2001
    num_years = year_end - year_start

    # L2
    decrease_per_year = 35 # decreased the price ... by $35
    total_decrease = decrease_per_year * num_years

    # L3
    price_2001 = 1950 # price in 2001 was $1950
    price_2009 = price_2001 - total_decrease

    # FA
    answer = price_2009
    return answer