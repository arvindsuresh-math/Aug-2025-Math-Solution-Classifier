def solve():
    """Index: 2646.
    Returns: the total cost to send the kid to school for 13 years.
    """
    # L1
    cost_per_semester = 20000 # $20,000 per semester
    semesters_per_year = 2 # 2 semesters in the year
    cost_per_year = cost_per_semester * semesters_per_year

    # L2
    years_of_school = 13 # 13 years of school
    total_cost = cost_per_year * years_of_school

    # FA
    answer = total_cost
    return answer