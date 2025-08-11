def solve():
    """Index: 1503.
    Returns: the total number of people on Jerome's contact list.
    """
    # L1
    classmates_count = 20 # 20 classmates on his cell phone contact list
    half_divisor = 2 # half as many out of school friends
    out_of_school_friends = classmates_count / half_divisor

    # L2
    parents_count = 2 # two parents
    sister_count = 1 # his sister
    family_members = parents_count + sister_count

    # L3
    total_people = classmates_count + out_of_school_friends + family_members

    # FA
    answer = total_people
    return answer