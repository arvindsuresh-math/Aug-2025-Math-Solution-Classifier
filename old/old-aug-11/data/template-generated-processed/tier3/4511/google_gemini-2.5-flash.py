def solve():
    """Index: 4511.
    Returns: the number of chocolate squares each student gets.
    """
    # L1
    gerald_bars = 7 # He brings 7 total bars
    teacher_multiplier = 2 # she will bring two more identical ones
    teacher_bars = gerald_bars * teacher_multiplier

    # L2
    total_bars = gerald_bars + teacher_bars

    # L3
    squares_per_bar = 8 # Each bar contains 8 squares
    total_squares = total_bars * squares_per_bar

    # L4
    num_students = 24 # There are 24 students in class
    squares_per_student = total_squares / num_students

    # FA
    answer = squares_per_student
    return answer