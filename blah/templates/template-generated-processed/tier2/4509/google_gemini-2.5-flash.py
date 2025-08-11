def solve():
    """Index: 4509.
    Returns: the number of people living in the apartment complex at 75% occupancy.
    """
    # L1
    two_person_apartments_count = 20 # 20 2 person apartments
    people_per_two_person_apartment = 2 # 2 person apartments
    people_in_two_person_apartments = two_person_apartments_count * people_per_two_person_apartment

    # L2
    four_person_apartments_count = 5 # 5 4 person apartments
    people_per_four_person_apartment = 4 # 4 person apartments
    people_in_four_person_apartments = four_person_apartments_count * people_per_four_person_apartment

    # L3
    studio_apartments_count = 10 # 10 studio apartments
    max_occupancy_per_building = studio_apartments_count + people_in_two_person_apartments + people_in_four_person_apartments

    # L4
    num_buildings = 4 # 4 identical buildings
    total_max_occupancy = num_buildings * max_occupancy_per_building

    # L5
    occupancy_rate_decimal = 0.75 # 75% of its maximum occupancy
    occupancy_rate_percent = 75 # 75% of its maximum occupancy
    current_occupancy = total_max_occupancy * occupancy_rate_decimal

    # FA
    answer = current_occupancy
    return answer