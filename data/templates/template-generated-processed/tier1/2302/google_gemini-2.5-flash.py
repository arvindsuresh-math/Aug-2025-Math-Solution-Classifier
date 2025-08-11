def solve():
    """Index: 2302.
    Returns: the price of the TV in 2009.
    """
    # L1
    end_year = 2009 # price in 2009
    start_year = 2001 # price in 2001
    period_years = end_year - start_year

    # L2
    decrease_per_year = 35 # decreased the price of a certain model of TV by $35
    total_decrease = decrease_per_year * period_years

    # L3
    initial_price = 1950 # price in 2001 was $1950
    price_in_2009 = initial_price - total_decrease

    # FA
    answer = price_in_2009
    return answer