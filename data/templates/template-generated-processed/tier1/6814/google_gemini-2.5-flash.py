def solve():
    """Index: 6814.
    Returns: the total number of people going to the museum.
    """
    # L1
    first_bus_people = 12 # If the first bus has 12 people
    multiplier_second_bus = 2 # twice the number of people on it as the first bus
    second_bus_people = first_bus_people * multiplier_second_bus

    # L2
    fewer_than_second_bus = 6 # 6 fewer people than the second bus
    third_bus_people = second_bus_people - fewer_than_second_bus

    # L3
    more_than_first_bus = 9 # 9 more people than the first bus
    fourth_bus_people = first_bus_people + more_than_first_bus

    # L4
    total_people = first_bus_people + second_bus_people + third_bus_people + fourth_bus_people

    # FA
    answer = total_people
    return answer