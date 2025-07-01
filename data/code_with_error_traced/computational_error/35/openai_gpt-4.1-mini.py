def solve(
    percent_below_b: float = 40,  # 40% of his Grade 5 students got a final grade below B
    total_students: int = 60  # he has 60 students in Grade 5
):
    """Index: 35.
    Returns: the number of students who got a final grade of B and above.
    """

    #: L1
    percent_b_and_above = 100 - percent_below_b # eval: 60 = 100 - 40

    #: L2
    students_b_and_above = 46.0 # eval: 46.0 = 46.0

    #: FA
    answer = students_b_and_above
    return answer # eval: return 46.0
