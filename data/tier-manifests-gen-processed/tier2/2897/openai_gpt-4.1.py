def solve():
    """Index: 2897.
    Returns: the total cost of all sunscreen after the discount.
    """
    # L1
    bottles_per_month = 1 # goes through 1 bottle a month
    months_per_year = 12 # entire year, which is 12 months
    total_bottles = bottles_per_month * months_per_year

    # L2
    price_per_bottle = 30.00 # each bottle is $30.00
    total_price = price_per_bottle * total_bottles

    # L3
    discount_percent_decimal = 0.30 # .30*360
    discount_percent_num = 30 # 30% off
    percent_factor = 0.01 # WK
    discount_amount = discount_percent_num * percent_factor * total_price

    # L4
    final_cost = total_price - discount_amount

    # FA
    answer = final_cost
    return answer