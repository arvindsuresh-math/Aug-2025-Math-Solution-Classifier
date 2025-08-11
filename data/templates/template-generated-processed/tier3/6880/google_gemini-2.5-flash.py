def solve():
    """Index: 6880.
    Returns: the number of mosquito bites each member of the rest of Cyrus' family has.
    """
    # L1
    bites_arms_legs = 14 # 14 mosquito bites on his arms and legs
    bites_body = 10 # another 10 on his body
    total_cyrus_bites = bites_arms_legs + bites_body

    # L2
    family_bites_divisor = 2 # half the number of bites that Cyrus got
    total_family_bites = total_cyrus_bites / family_bites_divisor

    # L3
    num_family_members = 6 # family of 6 other people
    bites_per_family_member = total_family_bites / num_family_members

    # FA
    answer = bites_per_family_member
    return answer