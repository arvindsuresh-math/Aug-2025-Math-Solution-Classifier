def solve():
    """Index: 329.
    Returns: the number of doughnuts each person will receive.
    """
    # L1
    samuel_dozens = 2 # Samuel bought 2 dozen doughnuts
    dozen = 12 # WK
    samuel_doughnuts = samuel_dozens * dozen

    # L2
    cathy_dozens = 3 # Cathy bought 3 dozen doughnuts
    cathy_doughnuts = cathy_dozens * dozen

    # L3
    total_doughnuts = samuel_doughnuts + cathy_doughnuts

    # L4
    friends = 8 # 8 other friends
    samuel = 1 # Samuel
    cathy = 1 # Cathy
    total_people = friends + samuel + cathy

    # L5
    doughnuts_per_person = total_doughnuts / total_people

    # FA
    answer = doughnuts_per_person
    return answer