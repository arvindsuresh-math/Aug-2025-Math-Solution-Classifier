def solve():
    """Index: 4821.
    Returns: the total amount Joanie will pay for the gym for the first 3 years.
    """
    # L1
    cost_per_month = 12 # $12 per month
    months_per_year = 12 # WK
    cost_per_year = cost_per_month * months_per_year

    # L2
    num_years = 3 # first 3 years
    total_membership_fee = cost_per_year * num_years

    # L3
    down_payment = 50 # $50 down payment
    total_cost = total_membership_fee + down_payment

    # FA
    answer = total_cost
    return answer