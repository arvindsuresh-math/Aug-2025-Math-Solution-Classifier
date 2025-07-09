def solve(
    total_students: int = 60, # If he surveyed 60 students
    fraction_high_allowance: float = 2/3, # 2/3 of the students receive an average of $6 allowance per day
    high_allowance: int = 6, # an average of $6 allowance per day
    low_allowance: int = 4 # the rest gets an average of $4 a day
):
    """Index: 58.
    Returns: the total amount of money those 60 students get in a day.
    """

    #: L1
    num_students_high_allowance = total_students * fraction_high_allowance # eval: 40.0 = 60 * 0.6666666666666666

    #: L2
    num_students_low_allowance = total_students - num_students_high_allowance # eval: 20.0 = 60 - 40.0

    #: L3
    total_allowance_high = low_allowance * high_allowance # eval: 24 = 4 * 6

    #: L4
    total_allowance_low = num_students_low_allowance * low_allowance # eval: 80.0 = 20.0 * 4

    #: L5
    total_daily_allowance = total_allowance_high + total_allowance_low # eval: 104.0 = 24 + 80.0

    #: FA
    answer = total_daily_allowance
    return answer # eval: return 104.0
