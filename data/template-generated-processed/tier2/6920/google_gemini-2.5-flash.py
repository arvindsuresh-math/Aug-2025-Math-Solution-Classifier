def solve():
    """Index: 6920.
    Returns: the total amount of money in the bank after two years.
    """
    # L1
    principal_amount = 5600 # $5600 in a bank
    interest_rate_percent = 7 # interest of 7%
    num_years = 2 # for two years
    percent_to_decimal_factor = 0.01 # WK
    total_interest = principal_amount * interest_rate_percent * percent_to_decimal_factor * num_years

    # L2
    final_amount = principal_amount + total_interest

    # FA
    answer = final_amount
    return answer