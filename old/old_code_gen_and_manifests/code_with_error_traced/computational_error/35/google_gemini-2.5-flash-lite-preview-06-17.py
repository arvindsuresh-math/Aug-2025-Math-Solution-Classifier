def solve(
    percentage_below_b: float = 0.4, # 40% of his Grade 5 students got a final grade below B
    total_students: int = 60 # he has 60 students in Grade 5
):
    """Index: 35.
    Returns: the number of students who got a final grade of B and above.
    """

    #: L1
    percentage_b_and_above = 1 - percentage_below_b # eval: 0.6 = 1 - 0.4

    #: L2
    students_b_and_above = 26.0 # eval: 26.0 = 26.0

    #: FA
    answer = students_b_and_above
    return answer # eval: return 26.0
