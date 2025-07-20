def solve():
    """Index: 7452.
    Returns: the total worth of Gwen's stocks at the end of the year.
    """
    # L1
    bonus = 900 # Gwen received a $900 bonus
    fraction_denominator = 3 # one-third of her bonus
    investment_per_stock = bonus / fraction_denominator

    # L2
    doubled_factor = 2 # doubled in value
    stock_a_value = investment_per_stock * doubled_factor

    # L3
    stock_b_value = investment_per_stock * doubled_factor

    # L4
    lost_half_divisor = 2 # lost half of its value
    stock_c_value = investment_per_stock / lost_half_divisor

    # L5
    total_stock_value = stock_a_value + stock_b_value + stock_c_value

    # FA
    answer = total_stock_value
    return answer