def solve():
    """Index: 4840.
    Returns: the number of donuts each student who likes donuts gets to eat.
    """
    # L1
    num_dozens = 4 # 4 dozen donuts
    donuts_per_dozen = 12 # WK
    total_donuts = num_dozens * donuts_per_dozen

    # L2
    total_students = 30 # 30 students in class
    liking_donuts_percent = 0.8 # 80% like donuts
    students_liking_donuts = total_students * liking_donuts_percent

    # L3
    donuts_per_liking_student = total_donuts / students_liking_donuts

    # FA
    answer = donuts_per_liking_student
    return answer