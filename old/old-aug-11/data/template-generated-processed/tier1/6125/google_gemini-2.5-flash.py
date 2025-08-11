def solve():
    """Index: 6125.
    Returns: the total time in seconds it took to finish the relay race.
    """
    # L1
    athlete_1_time = 55 # Athlete 1 ran for 55 seconds
    athlete_2_more_than_1 = 10 # athlete 2 ran 10 seconds more than athlete 1
    athlete_2_time = athlete_1_time + athlete_2_more_than_1

    # L2
    athlete_3_less_than_2 = 15 # athlete 3 ran 15 seconds less than athlete 2
    athlete_3_time = athlete_2_time - athlete_3_less_than_2

    # L3
    athlete_4_less_than_1 = 25 # athlete four finished it 25 seconds less than athlete 1
    athlete_4_time = athlete_1_time - athlete_4_less_than_1

    # L4
    total_time = athlete_1_time + athlete_2_time + athlete_3_time + athlete_4_time

    # FA
    answer = total_time
    return answer