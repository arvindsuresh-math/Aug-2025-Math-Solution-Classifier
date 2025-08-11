def solve():
    """Index: 4565.
    Returns: the amount of money Yoque borrowed.
    """
    # L1
    monthly_payment = 15 # $15 per month
    num_months = 11 # 11 months
    total_paid = monthly_payment * num_months

    # L2
    base_percent_val = 100 # WK
    additional_percent_val = 10 # an additional 10% of the money she borrowed
    total_percent_val = base_percent_val + additional_percent_val

    # L3
    value_of_one_percent = total_paid / total_percent_val

    # L4
    borrowed_money_percent = 100 # WK
    money_borrowed = value_of_one_percent * borrowed_money_percent

    # FA
    answer = money_borrowed
    return answer