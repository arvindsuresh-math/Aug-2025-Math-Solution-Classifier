def solve():
    """Index: 1685.
    Returns: the total amount Clinton spends on lunch over 5 days.
    """
    # L1
    burger_meal_cost = 6.00 # burger meal for lunch for $6.00
    upsize_cost = 1.00 # up sizes his fries and drinks for $1.00 more
    daily_lunch_cost = burger_meal_cost + upsize_cost

    # L2
    num_days = 5 # every day for 5 days
    total_cost = daily_lunch_cost * num_days

    # FA
    answer = total_cost
    return answer