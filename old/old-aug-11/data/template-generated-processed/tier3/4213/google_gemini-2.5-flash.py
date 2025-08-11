def solve():
    """Index: 4213.
    Returns: the height of the flag.
    """
    # L1
    first_square_length = 8 # The first square is 8 feet by 5 feet
    first_square_width = 5 # The first square is 8 feet by 5 feet
    first_square_area = first_square_length * first_square_width

    # L2
    second_square_length = 10 # The second one is 10 feet by 7 feet
    second_square_width = 7 # The second one is 10 feet by 7 feet
    second_square_area = second_square_length * second_square_width

    # L3
    third_square_side = 5 # The third one is 5 feet by 5 feet
    third_square_area = third_square_side * third_square_side

    # L4
    total_square_footage = first_square_area + second_square_area + third_square_area

    # L5
    flag_length = 15 # If he wants his flag to be 15 feet long
    flag_height = total_square_footage / flag_length

    # FA
    answer = flag_height
    return answer