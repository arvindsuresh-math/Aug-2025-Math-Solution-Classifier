def solve():
    """Index: 4237.
    Returns: the length of the last part of the race.
    """
    # L1
    first_part_length = 15.5 # The first part of the race is 15.5 kilometers long
    second_third_part_length = 21.5 # The second and third parts are each 21.5 kilometers long
    num_parts_same_length = 2 # WK
    sum_of_first_three_parts = first_part_length + (num_parts_same_length * second_third_part_length)

    # L2
    total_race_length = 74.5 # The total length of the race was 74.5 kilometers
    last_part_length = total_race_length - sum_of_first_three_parts

    # FA
    answer = last_part_length
    return answer