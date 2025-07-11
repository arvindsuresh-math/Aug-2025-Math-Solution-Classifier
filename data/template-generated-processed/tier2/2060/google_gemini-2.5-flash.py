def solve():
    """Index: 2060.
    Returns: the amount of milk left over.
    """
    # L1
    total_milk_provided = 16 # 16 cups of milk per day
    kids_consumption_percent_value = 75 # 75% of the milk
    kids_consumption_decimal = 0.75 # 75% so they drink 16*.75
    kids_consumed_milk = total_milk_provided * kids_consumption_decimal

    # L2
    milk_after_kids = total_milk_provided - kids_consumed_milk

    # L3
    cooking_percent_value = 50 # 50% of the remaining milk
    cooking_percent_decimal = 0.50 # .50*4
    percent_factor = 0.01 # WK
    milk_used_for_cooking = cooking_percent_value * percent_factor * milk_after_kids

    # L4
    milk_left_over = milk_after_kids - milk_used_for_cooking

    # FA
    answer = milk_left_over
    return answer