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
    students_with_four_dollars = total_students - students_with_six_dollars # eval: 20.0 = 60 - 40.0
    #: L3
    total_allowance_six_dollars = students_with_six_dollars * allowance_six_dollars # eval: 240.0 = 40.0 * 6
    #: L4
    total_allowance_four_dollars = students_with_four_dollars * allowance_four_dollars # eval: 80.0 = 20.0 * 4
    #: L5
    total_daily_allowance = total_allowance_six_dollars + total_allowance_four_dollars # eval: 320.0 = 240.0 + 80.0
    answer = total_daily_allowance  # FINAL ANSWER # eval: 320.0 = 320.0  # FINAL ANSWER
    return answer # eval: return 320.0