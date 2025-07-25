def solve():
    """Index: 6901.
    Returns: the number of friends who ate pizza with Ron.
    """
    # L2
    total_slices = 12 # 12-slice pizza
    slices_per_person = 4 # each of them ate 4 slices
    total_people_eating = total_slices / slices_per_person

    # L4
    ron_count = 1 # WK
    number_of_friends = total_people_eating - ron_count

    # L5
    # FA
    answer = number_of_friends
    return answer