def solve():
    """Index: 2342.
    Returns: the total amount the customer paid in all for 4 months after discount.
    """
    # L1
    monthly_rate = 50 # monthly internet rate is $50
    discount_percent = 5 # 5% discount
    percent_factor = 0.01 # WK
    discount_per_month = monthly_rate * discount_percent * percent_factor

    # L2
    num_months = 4 # 4 months
    total_discount = discount_per_month * num_months

    # L3
    total_without_discount = monthly_rate * num_months

    # L4
    total_paid = total_without_discount - total_discount

    # FA
    answer = total_paid
    return answer