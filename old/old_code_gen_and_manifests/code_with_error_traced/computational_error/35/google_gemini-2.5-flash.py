def solve(
        percentage_below_b: float = 0.40, # 40% of his Grade 5 students got a final grade below B
        total_students: int = 60 # he has 60 students in Grade 5
    ):
    """Index: 35.
    Returns: the number of students who got a final grade of B and above.
    """

    #: L1
    percentage_b_and_above = -0.4 # eval: -0.4 = -0.4

    #: L2
    students_b_and_above = total_students * percentage_b_and_above # eval: -24.0 = 60 * -0.4

    #: FA
    answer = students_b_and_above
    return answer # eval: return -24.0
