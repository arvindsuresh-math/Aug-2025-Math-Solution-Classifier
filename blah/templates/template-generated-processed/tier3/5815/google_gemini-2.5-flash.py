def solve():
    """Index: 5815.
    Returns: the original price of the car.
    """
    # L1
    spent_price = 7500 # $7500 on a used car
    discount_percentage = 25 # 25% less than the original price
    total_percentage = 100 # WK
    percentage_of_original_price = total_percentage - discount_percentage

    # L2
    value_per_percent = spent_price / percentage_of_original_price

    # L3
    original_price = value_per_percent * total_percentage

    # FA
    answer = original_price
    return answer