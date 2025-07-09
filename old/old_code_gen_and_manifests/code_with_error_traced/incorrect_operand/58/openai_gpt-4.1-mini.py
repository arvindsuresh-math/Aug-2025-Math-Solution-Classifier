def solve(
    total_students: int = 60,  # he surveyed 60 students
    fraction_with_six_dollars: float = 2/3,  # 2/3 of the students receive an average of $6 allowance per day
    allowance_six_dollars: int = 6,  # average $6 allowance per day
    allowance_four_dollars: int = 4  # the rest gets an average of $4 a day
):
    """Index: 58.
    Returns: the total amount of money those 60 students get in a day.
    """

    #: L1
    students_with_six_dollars = total_students * fraction_with_six_dollars # eval: 40.0 = 60 * 0.6666666666666666

    #: L2
    students_with_four_dollars = allowance_four_dollars - students_with_six_dollars # eval: -36.0 = 4 - 40.0

    #: L3
    total_allowance_six_dollars = students_with_six_dollars * allowance_six_dollars # eval: 240.0 = 40.0 * 6

    #: L4
    total_allowance_four_dollars = students_with_four_dollars * allowance_four_dollars # eval: -144.0 = -36.0 * 4

    #: L5
    total_daily_allowance = total_allowance_six_dollars + total_allowance_four_dollars # eval: 96.0 = 240.0 + -144.0

    #: FA
    answer = total_daily_allowance
    return answer # eval: return 96.0
