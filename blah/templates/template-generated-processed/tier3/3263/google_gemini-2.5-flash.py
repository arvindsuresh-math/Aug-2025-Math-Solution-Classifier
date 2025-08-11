def solve():
    """Index: 3263.
    Returns: the total number of cavities Andy gets.
    """
    # L1
    canes_per_teacher = 3 # 3 candy canes each from 4 teachers
    num_teachers = 4 # 4 teachers
    canes_from_teachers = canes_per_teacher * num_teachers

    # L2
    canes_from_parents = 2 # 2 candy canes from his parents
    canes_from_teachers_and_parents = canes_from_teachers + canes_from_parents

    # L3
    buy_divisor = 7 # 1/7 as many candy canes
    canes_bought = canes_from_teachers_and_parents / buy_divisor

    # L4
    total_canes = canes_bought + canes_from_teachers_and_parents

    # L5
    canes_per_cavity = 4 # every 4 candy canes he eats
    num_cavities = total_canes / canes_per_cavity

    # FA
    answer = num_cavities
    return answer