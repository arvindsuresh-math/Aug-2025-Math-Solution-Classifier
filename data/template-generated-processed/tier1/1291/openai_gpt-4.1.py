def solve():
    """Index: 1291.
    Returns: the number of second graders in Ms. Watson’s class.
    """
    # L1
    num_kindergartners = 14 # 14 kindergartners
    num_first_graders = 24 # 24 first graders
    k_and_1st = num_kindergartners + num_first_graders

    # L2
    total_students = 42 # Overall Ms. Watson has 42 students
    num_second_graders = total_students - k_and_1st

    # FA
    answer = num_second_graders
    return answer