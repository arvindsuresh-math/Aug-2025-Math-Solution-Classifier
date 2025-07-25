def solve():
    """Index: 3749.
    Returns: the total cost to buy enough bottles for 2 weeks.
    """
    # L1
    servings_per_container = 6 # 6 servings per container
    container_consumption_divisor = 2 # half a container a day
    servings_per_day = servings_per_container / container_consumption_divisor

    # L2
    days_per_week = 7 # WK
    num_weeks = 2 # 2 weeks
    total_days = days_per_week * num_weeks

    # L3
    total_servings_needed = servings_per_day * total_days

    # L4
    bottles_needed = total_servings_needed / servings_per_container

    # L5
    cost_per_bottle = 3.00 # $3.00 a bottle
    total_cost = cost_per_bottle * bottles_needed

    # FA
    answer = total_cost
    return answer