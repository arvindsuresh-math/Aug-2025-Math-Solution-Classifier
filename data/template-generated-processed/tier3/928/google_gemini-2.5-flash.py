def solve():
    """Index: 928.
    Returns: the number of female members in the glee club.
    """
    # L1
    female_to_male_ratio = 2 # two times as many female than male members
    male_parts = 1 # WK
    total_parts = female_to_male_ratio + male_parts

    # L2
    total_members = 18 # 18 members in the club
    members_per_group = total_members / total_parts

    # L3
    female_members = members_per_group * female_to_male_ratio

    # FA
    answer = female_members
    return answer