def solve():
    """Index: 4206.
    Returns: the number of bags of special dog food the family will need to buy.
    """
    # L1
    first_period_days = 60 # first 60 days of its life
    food_per_day_first_period = 2 # 2 ounces of this special dog food per day during the first 60 days
    food_consumed_first_period = first_period_days * food_per_day_first_period

    # L2
    days_in_year = 365 # WK
    food_per_day_second_period = 4 # 4 ounces per day of the special food
    remaining_days = days_in_year - first_period_days
    food_consumed_second_period = remaining_days * food_per_day_second_period

    # L3
    total_food_ounces = food_consumed_first_period + food_consumed_second_period

    # L4
    bag_size_pounds = 5 # 5-pound bags
    ounces_per_pound = 16 # WK
    ounces_per_bag = bag_size_pounds * ounces_per_pound

    # L5
    exact_bags_needed = total_food_ounces / ounces_per_bag

    # FA
    answer = 17
    return answer