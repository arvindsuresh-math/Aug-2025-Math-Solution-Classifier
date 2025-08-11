def solve():
    """Index: 4529.
    Returns: the total cost to hire builders for the project.
    """
    # L1
    new_builders = 6 # 6 builders
    initial_builders = 3 # 3 builders
    speed_multiplier = new_builders / initial_builders

    # L2
    initial_days_per_floor = 30 # 30 days
    days_per_floor_6_builders = initial_days_per_floor / speed_multiplier

    # L3
    num_houses = 5 # 5 houses
    floors_per_house = 6 # 6 floors each
    total_floors = num_houses * floors_per_house

    # L4
    total_days_for_project = days_per_floor_6_builders * total_floors

    # L5
    daily_pay_per_builder = 100 # $100 for a single day’s work
    num_builders_hired = 6 # 6 builders
    total_cost = total_days_for_project * daily_pay_per_builder * num_builders_hired

    # FA
    answer = total_cost
    return answer