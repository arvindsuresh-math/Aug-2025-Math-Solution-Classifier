def solve():
    """Index: 826.
    Returns: the total cost James pays for 2 semesters.
    """
    # L1
    units_per_semester = 20 # 20 units per semester
    cost_per_unit = 50 # each unit costs $50
    cost_per_semester = units_per_semester * cost_per_unit

    # L2
    num_semesters = 2 # for 2 semesters
    total_cost = cost_per_semester * num_semesters

    # FA
    answer = total_cost
    return answer