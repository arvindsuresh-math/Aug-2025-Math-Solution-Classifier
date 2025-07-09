def solve(
        fraction_students_group1: float = 2/3, # 2/3 of the students
        allowance_group1: int = 6, # receive an average of $6 allowance per day
        allowance_group2: int = 4, # the rest gets an average of $4 a day
        total_students_surveyed: int = 60 # If he surveyed 60 students
    ):
    """Index: 58.
    Returns: the total amount of money those 60 students get in a day.
    """
    #: L1
    num_students_group1 = total_students_surveyed * fraction_students_group1

    #: L2
    num_students_group2 = total_students_surveyed - num_students_group1

    #: L3
    total_allowance_group1 = num_students_group1 * allowance_group1

    #: L4
    total_allowance_group2 = num_students_group2 * allowance_group2

    #: L5
    total_daily_allowance = total_allowance_group1 + total_allowance_group2

    answer = total_daily_allowance # FINAL ANSWER
    return answer