def solve():
    """Index: 2128.
    Returns: the number of water jugs the custodian will fill.
    """
    # L1
    students = 200 # 200 students
    cups_per_student = 10 # 10 cups of water
    total_cups_needed = students * cups_per_student

    # L2
    cups_per_jug = 40 # 40 cups of water
    num_jugs = total_cups_needed / cups_per_jug

    # FA
    answer = num_jugs
    return answer