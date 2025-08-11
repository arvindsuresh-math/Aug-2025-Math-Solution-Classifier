def solve():
    """Index: 1265.
    Returns: the average monthly bill for the family.
    """
    # L1
    avg_bill_first_period = 30 # $30 a month
    duration_first_period = 4 # first 4 months
    sum_bills_first_period = avg_bill_first_period * duration_first_period

    # L2
    avg_bill_second_period = 24 # $24 a month
    duration_second_period = 2 # last 2 months
    sum_bills_second_period = avg_bill_second_period * duration_second_period

    # L3
    total_sum_bills = sum_bills_first_period + sum_bills_second_period

    # L4
    total_months = 6 # all 6 months
    average_monthly_bill = total_sum_bills / total_months

    # FA
    answer = average_monthly_bill
    return answer