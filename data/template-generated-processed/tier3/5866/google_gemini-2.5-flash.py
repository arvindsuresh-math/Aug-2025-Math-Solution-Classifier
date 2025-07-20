def solve():
    """Index: 5866.
    Returns: the total number of chairs needed for the ceremony.
    """
    # L1
    num_graduates = 50 # 50 graduates
    parents_per_graduate = 2 # 2 parents
    num_parents = num_graduates * parents_per_graduate

    # L2
    num_teachers = 20 # Twenty teachers
    administrator_divisor = 2 # half as many administrators
    num_administrators = num_teachers / administrator_divisor

    # L3
    total_chairs = num_graduates + num_parents + num_teachers + num_administrators

    # FA
    answer = total_chairs
    return answer