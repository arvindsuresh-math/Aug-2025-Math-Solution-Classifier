def solve():
    """Index: 5414.
    Returns: the number of more minutes Peter has to walk.
    """
    # L1
    total_miles_to_walk = 2.5 # 2.5 miles to get to the grocery store
    miles_already_walked = 1 # walked 1 mile already
    remaining_miles = total_miles_to_walk - miles_already_walked

    # L2
    minutes_per_mile = 20 # 20 minutes to walk one mile
    time_remaining = minutes_per_mile * remaining_miles

    # FA
    answer = time_remaining
    return answer