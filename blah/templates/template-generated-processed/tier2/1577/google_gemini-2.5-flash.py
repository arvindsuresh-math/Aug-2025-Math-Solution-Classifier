def solve():
    """Index: 1577.
    Returns: the amount of money in the account after two years.
    """
    # L1
    initial_deposit = 100 # He puts $100 in it
    interest_rate_decimal = 0.1 # earns 10% interest every year
    interest_year1 = initial_deposit * interest_rate_decimal

    # L2
    annual_deposit = 10 # and then 10 each year
    balance_after_year1 = initial_deposit + interest_year1 + annual_deposit

    # L3
    interest_year2 = balance_after_year1 * interest_rate_decimal

    # L4
    balance_after_year2 = balance_after_year1 + interest_year2 + annual_deposit

    # FA
    answer = balance_after_year2
    return answer