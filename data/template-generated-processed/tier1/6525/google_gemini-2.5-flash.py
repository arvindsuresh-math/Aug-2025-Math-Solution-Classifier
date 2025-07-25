def solve():
    """Index: 6525.
    Returns: the total number of eyes the whole monster family had.
    """
    # L1
    mom_eyes = 1 # 1 eye
    dad_eyes = 3 # 3
    parent_eyes = mom_eyes + dad_eyes

    # L2
    num_kids = 3 # 3 kids
    eyes_per_kid = 4 # 4 eyes each
    child_eyes = num_kids * eyes_per_kid

    # L3
    total_eyes = parent_eyes + child_eyes

    # FA
    answer = total_eyes
    return answer