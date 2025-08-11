def solve():
    """Index: 6293.
    Returns: the total amount of money John has after 3 years.
    """
    # L1
    principal = 1000 # invests $1000
    interest_rate_decimal = 0.1 # 10% simple interest
    annual_interest = principal * interest_rate_decimal

    # L2
    num_years = 3 # after 3 years
    total_interest = annual_interest * num_years

    # L3
    total_money = total_interest + principal

    # FA
    answer = total_money
    return answer