def solve():
    """Index: 2060.
    Returns: the amount of milk left over after Daisy's kids and cooking use.
    """
    # L1
    total_milk = 16 # 16 cups of milk per day
    kids_percent_decimal = 0.75 # 75% of the milk is consumed by Daisy’s kids
    kids_milk = total_milk * kids_percent_decimal

    # L2
    remaining_milk = total_milk - kids_milk

    # L3
    cook_percent_num = 50 # 50% of the remaining milk
    cook_percent_decimal = 0.50 # .50*4
    percent_factor = 0.01 # WK
    cook_milk = cook_percent_num * percent_factor * remaining_milk

    # L4
    milk_left = remaining_milk - cook_milk

    # FA
    answer = milk_left
    return answer