def solve():
    """Index: 3675.
    Returns: the total amount in fees George will have to pay.
    """
    # L1
    loan_amount = 100 # borrow $100
    initial_fee_percent_num = 5 # finance fee starts at 5%
    percent_factor = 0.01 # WK
    fee_week1 = loan_amount * initial_fee_percent_num * percent_factor

    # L2
    doubling_factor = 2 # doubles every week
    fee_percent_week2_num = initial_fee_percent_num * doubling_factor

    # L3
    fee_week2 = loan_amount * fee_percent_week2_num * percent_factor

    # L4
    total_fees = fee_week1 + fee_week2

    # FA
    answer = total_fees
    return answer