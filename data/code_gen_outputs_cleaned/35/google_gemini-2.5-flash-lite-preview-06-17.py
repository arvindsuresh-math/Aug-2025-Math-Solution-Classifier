def solve(
    percentage_below_b: float = 0.4, # 40% of his Grade 5 students got a final grade below B
    total_students: int = 60 # he has 60 students in Grade 5
):
    """Index: 35.
    Returns: the number of students who got a final grade of B and above.
    """
    #: L1
    percentage_b_and_above = 1 - percentage_below_b

    #: L2
    students_b_and_above = total_students * percentage_b_and_above

    answer = students_b_and_above # FINAL ANSWER
    return answer