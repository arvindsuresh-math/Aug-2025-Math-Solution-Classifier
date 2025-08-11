def solve():
    """Index: 6660.
    Returns: the number of hours James will have to work to pay for everything.
    """
    # L1
    meat_cost_per_pound = 5 # $5/pound
    meat_pounds = 20 # 20 wasted pounds of meat
    total_meat_cost = meat_cost_per_pound * meat_pounds

    # L2
    veg_cost_per_pound = 4 # $4/pound
    veg_pounds = 15 # 15 wasted pounds of fruits and vegetables
    total_veg_cost = veg_cost_per_pound * veg_pounds

    # L3
    bread_cost_per_pound = 1.50 # $1.50/pound
    bread_pounds = 60 # 60 wasted pounds of bread products
    total_bread_cost = bread_cost_per_pound * bread_pounds

    # L4
    janitor_normal_wage = 10 # normally make $10/hour
    time_and_a_half_factor = 1.5 # WK
    janitor_time_and_a_half_wage = janitor_normal_wage * time_and_a_half_factor

    # L5
    janitor_hours = 10 # 10 hours of time-and-a-half pay
    total_janitor_cost = janitor_time_and_a_half_wage * janitor_hours

    # L6
    total_cost_owed = total_meat_cost + total_veg_cost + total_bread_cost + total_janitor_cost

    # L7
    james_hourly_wage = 8 # minimum wage ($8)
    hours_to_work = total_cost_owed / james_hourly_wage

    # FA
    answer = hours_to_work
    return answer