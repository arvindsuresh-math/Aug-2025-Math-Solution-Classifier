def solve():
    """Index: 252.
    Returns: the number of days the coffee will last.
    """
    # L1
    coffee_lbs = 3 # 3 lbs. of coffee
    cups_per_lb = 40 # 40 cups of coffee
    total_cups_of_coffee = coffee_lbs * cups_per_lb

    # L2
    cups_per_day = 3 # 3 cups of coffee every day
    days_coffee_lasts = total_cups_of_coffee / cups_per_day

    # FA
    answer = days_coffee_lasts
    return answer