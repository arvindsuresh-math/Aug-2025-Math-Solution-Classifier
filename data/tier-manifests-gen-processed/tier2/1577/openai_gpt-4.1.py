def solve():
    """Index: 1577.
    Returns: the amount of money in the account after two years.
    """
    # L1
    initial_deposit = 100 # puts $100 in it
    interest_rate = 0.1 # earns 10% interest every year
    annual_deposit = 10 # 10 each year
    first_year_interest = initial_deposit * interest_rate

    # L2
    first_year_total = initial_deposit + first_year_interest + annual_deposit

    # L3
    second_year_interest = first_year_total * interest_rate

    # L4
    second_year_total = first_year_total + second_year_interest + annual_deposit

    # FA
    answer = second_year_total
    return answer