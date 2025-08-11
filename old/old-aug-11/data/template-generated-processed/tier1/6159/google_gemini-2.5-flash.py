def solve():
    """Index: 6159.
    Returns: the total money the restaurant made throughout the day.
    """
    # L1
    meals_set1_quantity = 10 # 10 meals
    meals_set1_price = 8 # $8 each
    earnings_set1 = meals_set1_quantity * meals_set1_price

    # L2
    meals_set2_quantity = 5 # 5 meals
    meals_set2_price = 10 # $10 each
    earnings_set2 = meals_set2_quantity * meals_set2_price

    # L3
    meals_set3_quantity = 20 # 20 meals
    meals_set3_price = 4 # $4 each
    earnings_set3 = meals_set3_quantity * meals_set3_price

    # L4
    total_earnings = earnings_set1 + earnings_set2 + earnings_set3

    # FA
    answer = total_earnings
    return answer