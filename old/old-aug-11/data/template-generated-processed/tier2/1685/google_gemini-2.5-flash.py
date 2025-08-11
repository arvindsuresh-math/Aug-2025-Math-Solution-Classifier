def solve():
    """Index: 1685.
    Returns: the total amount Clinton spends on lunch.
    """
    # L1
    burger_meal_cost = 6.00 # $6.00
    upsize_cost = 1.00 # $1.00 more
    daily_meal_cost = burger_meal_cost + upsize_cost

    # L2
    number_of_days = 5 # for 5 days
    total_spent = daily_meal_cost * number_of_days

    # FA
    answer = total_spent
    return answer