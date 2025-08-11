def solve():
    """Index: 152.
    Returns: the discounted cost of the newspaper subscription.
    """
    # L1
    normal_cost = 80 # subscription normally costs $80
    discount_percentage_numerator = 45 # 45% discount
    percentage_denominator = 100 # 45% discount
    discount_amount = normal_cost * discount_percentage_numerator / percentage_denominator

    # L2
    discounted_cost = normal_cost - discount_amount

    # FA
    answer = discounted_cost
    return answer