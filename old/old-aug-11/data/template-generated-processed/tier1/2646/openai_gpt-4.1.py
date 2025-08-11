def solve():
    """Index: 2646.
    Returns: the total cost to send the kid to 13 years of school.
    """
    # L1
    cost_per_semester = 20000 # $20,000 per semester
    semesters_per_year = 2 # 2 semesters in the year
    yearly_cost = cost_per_semester * semesters_per_year

    # L2
    years = 13 # 13 years of school
    total_cost = yearly_cost * years

    # FA
    answer = total_cost
    return answer