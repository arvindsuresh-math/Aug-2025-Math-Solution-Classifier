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
    students_group1 = total_students * fraction_group1 # eval: 40.0 = 60 * 0.6666666666666666

    #: L2
    students_group2 = total_students - students_group1 # eval: 20.0 = 60 - 40.0

    #: L3

    #: L4
    total_allowance_group2 = students_group2 * avg_allowance_group2 # eval: 80.0 = 20.0 * 4

    #: L5
    total_daily_allowance = total_students + total_allowance_group2 # eval: 140.0 = 60 + 80.0

    #: FA
    answer = total_daily_allowance
    return answer # eval: return 140.0
