def solve():
    """Index: 1291.
    Returns: the number of second graders in Ms. Watson's class.
    """
    # L1
    kindergartners = 14 # 14 kindergartners
    first_graders = 24 # 24 first graders
    total_k_and_fg = kindergartners + first_graders

    # L2
    total_students = 42 # 42 students
    second_graders = total_students - total_k_and_fg

    # FA
    answer = second_graders
    return answer