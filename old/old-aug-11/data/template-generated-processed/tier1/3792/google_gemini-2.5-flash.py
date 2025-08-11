def solve():
    """Index: 3792.
    Returns: the number of members in the third group.
    """
    # L1
    first_group_members = 25 # The first group has 25 members
    second_group_members = 30 # the second group has 30 members
    members_first_two_groups = first_group_members + second_group_members

    # L2
    total_choir_members = 70 # the choir overall has 70 members
    third_group_members = total_choir_members - members_first_two_groups

    # FA
    answer = third_group_members
    return answer