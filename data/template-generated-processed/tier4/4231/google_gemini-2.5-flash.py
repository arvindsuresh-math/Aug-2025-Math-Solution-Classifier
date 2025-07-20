def solve():
    """Index: 4231.
    Returns: the total gallons of water needed.
    """
    # L1
    num_men = 25 # 25 men, including himself
    water_per_man_per_day = 0.5 # 1/2 a gallon of water per day per man
    water_needed_per_day = num_men * water_per_man_per_day

    # L2
    total_distance = 4000 # 4,000 miles
    boat_speed = 200 # 200 miles per day
    travel_days = total_distance / boat_speed

    # L3
    total_water_needed = travel_days * water_needed_per_day

    # FA
    answer = total_water_needed
    return answer