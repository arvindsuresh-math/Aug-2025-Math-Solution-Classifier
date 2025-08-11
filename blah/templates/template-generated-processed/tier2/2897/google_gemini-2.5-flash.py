def solve():
    """Index: 2897.
    Returns: the total cost of the sunscreen after the discount.
    """
    # L1
    bottles_per_month = 1 # 1 bottle of sunscreen a month
    months_per_year = 12 # WK
    bottles_needed = bottles_per_month * months_per_year

    # L2
    cost_per_bottle = 30.00 # each bottle is $30.00
    total_cost_before_discount = cost_per_bottle * bottles_needed

    # L3
    discount_percent_num = 30 # 30% off
    discount_percent_decimal = 0.30 # from solution text: .30*360
    percent_factor = 0.01 # WK
    discount_amount = discount_percent_num * percent_factor * total_cost_before_discount

    # L4
    final_cost = total_cost_before_discount - discount_amount

    # FA
    answer = final_cost
    return answer