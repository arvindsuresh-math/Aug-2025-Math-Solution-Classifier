def solve():
    """Index: 3748.
    Returns: the total number of aquariums Lucy could clean.
    """
    # L1
    total_hours_worked = 24 # working 24 hours this week
    hours_per_increment = 3 # 2 aquariums in 3 hours
    number_of_increments = total_hours_worked / hours_per_increment

    # L2
    aquariums_per_increment = 2 # clean 2 aquariums
    total_aquariums_cleaned = aquariums_per_increment * number_of_increments

    # FA
    answer = total_aquariums_cleaned
    return answer