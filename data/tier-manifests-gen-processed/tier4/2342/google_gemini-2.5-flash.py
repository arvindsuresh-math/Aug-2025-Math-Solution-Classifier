def solve():
    """Index: 2342.
    Returns: the total amount the customer paid for 4 months with discount.
    """
    # L1
    monthly_rate = 50 # monthly internet rate is $50
    discount_percentage_numerator = 5 # 5% discount
    percent_divisor = 100 # WK
    monthly_discount = monthly_rate * discount_percentage_numerator / percent_divisor

    # L2
    num_months = 4 # for 4 months
    total_discount = monthly_discount * num_months

    # L3
    total_cost_without_discount = monthly_rate * num_months

    # L4
    final_payment = total_cost_without_discount - total_discount

    # FA
    answer = final_payment
    return answer