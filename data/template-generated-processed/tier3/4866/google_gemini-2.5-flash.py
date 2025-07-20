def solve():
    """Index: 4866.
    Returns: the minimum number of students that can sit on each bench.
    """
    # L1
    female_multiplier = 4 # 4 times as many
    male_students = 29 # 29 male students
    female_students = female_multiplier * male_students

    # L2
    total_students = male_students + female_students

    # L3
    num_benches = 29 # 29 benches
    students_per_bench = total_students / num_benches

    # FA
    answer = students_per_bench
    return answer