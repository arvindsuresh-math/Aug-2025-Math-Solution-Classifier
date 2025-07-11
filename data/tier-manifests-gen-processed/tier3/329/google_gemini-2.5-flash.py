def solve():
    """Index: 329.
    Returns: the number of doughnuts each person will receive.
    """
    # L1
    dozen_value = 12 # WK
    samuel_dozens = 2 # Samuel bought 2 dozen doughnuts
    samuel_doughnuts = samuel_dozens * dozen_value

    # L2
    cathy_dozens = 3 # Cathy bought 3 dozen doughnuts
    cathy_doughnuts = cathy_dozens * dozen_value

    # L3
    total_doughnuts = samuel_doughnuts + cathy_doughnuts

    # L4
    other_friends = 8 # 8 other friends
    samuel_count = 1 # (Samuel)
    cathy_count = 1 # (Cathy)
    total_people = other_friends + samuel_count + cathy_count

    # L5
    doughnuts_per_person = total_doughnuts / total_people

    # FA
    answer = doughnuts_per_person
    return answer