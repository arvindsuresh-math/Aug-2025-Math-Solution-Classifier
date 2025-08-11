def solve():
    """Index: 7321.
    Returns: the total number of people who went on the field trip.
    """
    # L1
    num_vans = 9 # 9 vans
    people_per_van = 8 # 8 people in each van
    people_in_vans = num_vans * people_per_van

    # L2
    num_buses = 10 # 10 buses
    people_per_bus = 27 # 27 people on each bus
    people_in_buses = num_buses * people_per_bus

    # L3
    total_people = people_in_vans + people_in_buses

    # FA
    answer = total_people
    return answer