def solve():
    """Index: 7383.
    Returns: the number of groups formed.
    """
    # L1
    boys = 9 # 9 boys
    girls = 12 # 12 girls
    total_students = boys + girls

    # L2
    members_per_group = 3 # three members
    num_groups = total_students / members_per_group

    # FA
    answer = num_groups
    return answer