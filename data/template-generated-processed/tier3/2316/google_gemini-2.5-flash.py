def solve():
    """Index: 2316.
    Returns: the total number of students in the class, including Mary.
    """
    # L1
    initial_stickers = 50 # Mary brought 50 stickers
    stickers_left_over = 8 # she has 8 stickers left over
    stickers_given_out = initial_stickers - stickers_left_over

    # L2
    stickers_per_friend = 4 # gave 4 stickers to each
    number_of_friends = 5 # each of her 5 friends
    stickers_to_friends = stickers_per_friend * number_of_friends

    # L3
    stickers_to_rest_of_class = stickers_given_out - stickers_to_friends

    # L4
    stickers_per_other_student = 2 # everyone else in class two stickers each
    other_students = stickers_to_rest_of_class / stickers_per_other_student

    # L5
    mary = 1 # including Mary
    total_students_in_class = mary + number_of_friends + other_students

    # FA
    answer = total_students_in_class
    return answer