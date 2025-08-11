def solve():
    """Index: 3861.
    Returns: the total number of students all four primary schools can teach at a time.
    """
    # L1
    num_schools_group1 = 2 # Two of them
    capacity_school_group1 = 400 # teach 400 students at a time
    total_capacity_group1 = num_schools_group1 * capacity_school_group1

    # L2
    num_schools_group2 = 2 # the other two
    capacity_school_group2 = 340 # 340 students at a time
    total_capacity_group2 = num_schools_group2 * capacity_school_group2

    # L3
    total_capacity_all_schools = total_capacity_group1 + total_capacity_group2

    # FA
    answer = total_capacity_all_schools
    return answer