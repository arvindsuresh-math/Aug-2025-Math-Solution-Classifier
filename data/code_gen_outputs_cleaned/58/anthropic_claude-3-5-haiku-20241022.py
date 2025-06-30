def solve(
    total_students: int = 60,  # he surveyed 60 students
    fraction_students_high_allowance: float = 2/3,  # 2/3 of the students receive an average of $6 allowance per day
    high_daily_allowance: int = 6,  # $6 allowance per day
    low_daily_allowance: int = 4  # the rest gets an average of $4 a day
):
    """Index: 58.
    Returns: the total amount of money those 60 students get in a day.
    """
    #: L1
    num_students_high_allowance = total_students * fraction_students_high_allowance

    #: L2
    num_students_low_allowance = total_students - num_students_high_allowance

    #: L3
    total_high_allowance = num_students_high_allowance * high_daily_allowance

    #: L4
    total_low_allowance = num_students_low_allowance * low_daily_allowance

    #: L5
    total_daily_allowance = total_high_allowance + total_low_allowance

    answer = total_daily_allowance  # FINAL ANSWER
    return answer