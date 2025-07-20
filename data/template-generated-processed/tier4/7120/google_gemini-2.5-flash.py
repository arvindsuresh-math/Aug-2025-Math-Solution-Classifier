def solve():
    """Index: 7120.
    Returns: the total amount Adam's father will have.
    """
    # L1
    initial_deposit = 2000 # Adam's father deposited $2000
    interest_rate_percent_num = 8 # 8% interest
    percent_denominator = 100 # WK
    annual_interest = initial_deposit * interest_rate_percent_num / percent_denominator

    # L2
    num_years = 2.5 # 2 and a half years
    total_interest = annual_interest * num_years

    # L3
    final_amount = initial_deposit + total_interest

    # FA
    answer = final_amount
    return answer