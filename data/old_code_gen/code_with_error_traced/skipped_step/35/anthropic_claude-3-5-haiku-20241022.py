def solve(
        total_students: int = 60,  # Mr. Sanchez has 60 students in Grade 5
        percent_below_b: float = 0.4  # 40% of his students got a final grade below B
):
    """Index: 35.
    Returns: the number of students who got a final grade of B and above."""

    #: L1
    percent_b_and_above = 1 - percent_below_b # eval: 0.6 = 1 - 0.4

    #: L2

    #: FA
    answer = percent_below_b
    return answer # eval: return 0.4
