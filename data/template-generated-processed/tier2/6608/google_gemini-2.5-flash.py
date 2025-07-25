def solve():
    """Index: 6608.
    Returns: the total cost to replace all cardio machines.
    """
    # L1
    num_gyms = 20 # They have 20 gyms.
    bikes_per_gym = 10 # Each gym has 10 bikes
    total_bikes = num_gyms * bikes_per_gym

    # L2
    treadmills_per_gym = 5 # 5 treadmills
    ellipticals_per_gym = 5 # 5 elliptical machines
    total_treadmills_ellipticals_per_type = num_gyms * treadmills_per_gym

    # L3
    bike_cost_per_unit = 700 # The bikes cost $700 each.
    total_bike_cost = total_bikes * bike_cost_per_unit

    # L4
    treadmill_cost_factor = 1.5 # 50% more than that.
    treadmill_cost_per_unit = bike_cost_per_unit * treadmill_cost_factor

    # L5
    total_treadmill_cost = treadmill_cost_per_unit * total_treadmills_ellipticals_per_type

    # L6
    elliptical_cost_factor = 2 # twice as expensive
    elliptical_cost_per_unit = treadmill_cost_per_unit * elliptical_cost_factor

    # L7
    total_elliptical_cost = elliptical_cost_per_unit * total_treadmills_ellipticals_per_type

    # L8
    total_cost = total_bike_cost + total_treadmill_cost + total_elliptical_cost

    # FA
    answer = total_cost
    return answer