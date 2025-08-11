def solve():
    """Index: 6005.
    Returns: the total number of people the building houses.
    """
    # L1
    num_stories = 25 # A 25 story building
    apartments_per_floor = 4 # 4 apartments on each floor
    total_apartments = num_stories * apartments_per_floor

    # L2
    people_per_apartment = 2 # two people
    total_people = total_apartments * people_per_apartment

    # FA
    answer = total_people
    return answer