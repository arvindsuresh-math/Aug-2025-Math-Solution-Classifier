def solve():
    """Index: 252.
    Returns: the number of days the coffee will last Angie.
    """
    # L1
    pounds_of_coffee = 3 # Angie bought 3 lbs. of coffee
    cups_per_pound = 40 # Each lb. of coffee will brew about 40 cups
    total_cups = pounds_of_coffee * cups_per_pound

    # L2
    cups_per_day = 3 # Angie drinks 3 cups of coffee every day
    days = total_cups / cups_per_day

    # FA
    answer = days
    return answer