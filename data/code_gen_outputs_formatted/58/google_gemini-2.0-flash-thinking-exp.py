def solve(
    fraction_group1: float = 2/3, # 2/3 of the students
    avg_allowance_group1: int = 6, # receive an average of $6 allowance per day
    avg_allowance_group2: int = 4, # the rest gets an average of $4 a day
    total_students: int = 60 # If he surveyed 60 students
):
    """Index: 58.
    Returns: the total amount of money those 60 students get in a day.
    """

    #: L1
    students_group1 = total_students * fraction_group1

    #: L2
    students_group2 = total_students - students_group1

    #: L3
    total_allowance_group1 = students_group1 * avg_allowance_group1

    #: L4
    total_allowance_group2 = students_group2 * avg_allowance_group2

    #: L5
    total_daily_allowance = total_allowance_group1 + total_allowance_group2

    #: FA
    answer = total_daily_allowance
    return answer