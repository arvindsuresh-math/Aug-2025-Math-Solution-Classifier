def solve():
    """Index: 7352.
    Returns: the number of students catching up on homework.
    """
    # L1
    total_students = 24 # In the class of 24 students
    silent_reading_divisor = 2 # half are doing silent reading
    silent_reading_students = total_students / silent_reading_divisor

    # L2
    board_games_divisor = 3 # a third are playing board games
    board_game_students = total_students / board_games_divisor

    # L3
    accounted_students = silent_reading_students + board_game_students

    # L4
    homework_students = total_students - accounted_students

    # FA
    answer = homework_students
    return answer