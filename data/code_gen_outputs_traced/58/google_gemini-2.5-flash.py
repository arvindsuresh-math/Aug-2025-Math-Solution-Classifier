def solve(
        fraction_students_group1: float = 2/3, # 2/3 of the students
        allowance_group1: int = 6, # an average of $6 allowance per day
        allowance_group2: int = 4, # the rest gets an average of $4 a day
        total_students: int = 60 # If he surveyed 60 students
    ):
    """Index: 58.
    Returns: the total amount of money those 60 students get in a day.
    """

    #: L1
    num_students_group1 = total_students * fraction_students_group1 # eval: 40.0 = 60 * 0.6666666666666666

    #: L2
    num_students_group2 = total_students - num_students_group1 # eval: 20.0 = 60 - 40.0

    #: L3
    sum_allowance_group1 = num_students_group1 * allowance_group1 # eval: 240.0 = 40.0 * 6

    #: L4
    sum_allowance_group2 = num_students_group2 * allowance_group2 # eval: 80.0 = 20.0 * 4

    #: L5
    total_daily_amount = sum_allowance_group1 + sum_allowance_group2 # eval: 320.0 = 240.0 + 80.0

    #: FA
    answer = total_daily_amount # eval: 320.0 = 320.0
    return answer # eval: return 320.0
