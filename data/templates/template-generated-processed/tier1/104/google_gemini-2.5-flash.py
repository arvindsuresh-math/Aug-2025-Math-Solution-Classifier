def solve():
    """Index: 104.
    Returns: the total number of people the boat can transport in 2 days.
    """
    # L1
    people_per_trip = 12 # 12 people during one trip
    trips_per_day = 4 # 4 boat trips through the lake
    people_per_day = trips_per_day * people_per_trip

    # L2
    num_days = 2 # in 2 days
    total_people = people_per_day * num_days

    # FA
    answer = total_people
    return answer