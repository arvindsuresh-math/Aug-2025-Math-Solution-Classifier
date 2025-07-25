def solve():
    """Index: 826.
    Returns: the total amount James pays for 2 semesters.
    """
    # L1
    units_per_semester = 20 # James takes 20 units per semester
    cost_per_unit = 50 # each unit costs $50
    per_semester_cost = units_per_semester * cost_per_unit

    # L2
    num_semesters = 2 # 2 semesters
    total_cost = per_semester_cost * num_semesters

    # FA
    answer = total_cost
    return answer