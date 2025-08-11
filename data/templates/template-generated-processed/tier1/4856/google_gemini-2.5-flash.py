def solve():
    """Index: 4856.
    Returns: the total number of wheels on the floor.
    """
    # L1
    num_people = 40 # 40 people
    feet_per_person = 2 # 2 feet
    total_feet = num_people * feet_per_person

    # L2
    wheels_per_skate = 4 # 4 wheels
    total_wheels = total_feet * wheels_per_skate

    # FA
    answer = total_wheels
    return answer