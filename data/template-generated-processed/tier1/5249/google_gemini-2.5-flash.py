def solve():
    """Index: 5249.
    Returns: the total number of cakes Ginger makes in 10 years.
    """
    # L1
    num_children = 2 # 2 children
    holidays_per_child = 4 # 4 times a year
    cakes_for_children_per_year = num_children * holidays_per_child

    # L2
    cakes_for_husband_per_year = 6 # 6 cakes a year

    # L3
    num_parents = 2 # 2 parents
    birthdays_per_parent = 1 # only for their birthdays
    cakes_for_parents_per_year = num_parents * birthdays_per_parent

    # L4
    total_cakes_per_year = cakes_for_children_per_year + cakes_for_husband_per_year + cakes_for_parents_per_year

    # L5
    num_years = 10 # in 10 years
    total_cakes_in_10_years = total_cakes_per_year * num_years

    # FA
    answer = total_cakes_in_10_years
    return answer