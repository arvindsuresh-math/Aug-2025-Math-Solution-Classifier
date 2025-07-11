def solve():
    """Index: 1430.
    Returns: the number of parents at the park.
    """
    # L1
    num_groups = 3 # split into 3 equally sized playgroups
    people_per_group = 25 # each group contains 25 people
    total_people = num_groups * people_per_group

    # L2
    num_girls = 14 # 14 girls
    num_boys = 11 # 11 boys
    total_children = num_girls + num_boys

    # L3
    num_parents = total_people - total_children

    # FA
    answer = num_parents
    return answer