def solve():
    """Index: 4149.
    Returns: the number of cars that can still be accommodated by the parking garage.
    """
    # L1
    first_level_spaces = 90 # 90 parking spaces
    second_level_more_than_first = 8 # 8 more parking spaces than on the first level
    second_level_spaces = first_level_spaces + second_level_more_than_first

    # L2
    third_level_more_than_second = 12 # 12 more available parking spaces on the third level than on the second level
    third_level_spaces = second_level_spaces + third_level_more_than_second

    # L3
    fourth_level_fewer_than_third = 9 # 9 fewer parking spaces than the third level
    fourth_level_spaces = third_level_spaces - fourth_level_fewer_than_third

    # L4
    total_capacity = first_level_spaces + second_level_spaces + third_level_spaces + fourth_level_spaces

    # L5
    cars_already_parked = 100 # 100 cars are already parked
    remaining_capacity = total_capacity - cars_already_parked

    # FA
    answer = remaining_capacity
    return answer