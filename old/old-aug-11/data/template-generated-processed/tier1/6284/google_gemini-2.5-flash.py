def solve():
    """Index: 6284.
    Returns: the time it would take for the slower one of Lola and Tara to reach the top floor.
    """
    # L1
    num_stories = 20 # 20 story building
    lola_time_per_story = 10 # Lola can run up 1 story in 10 seconds
    lola_total_time = num_stories * lola_time_per_story

    # L2
    elevator_time_per_story = 8 # The elevator goes up a story in 8 seconds
    tara_travel_time = elevator_time_per_story * num_stories

    # L3
    elevator_stop_time_per_floor = 3 # stops for 3 seconds on every single floor
    tara_stop_time = num_stories * elevator_stop_time_per_floor

    # L4
    tara_total_time = tara_travel_time + tara_stop_time

    # L5
    # The question asks for the time of the slower one. Lola's time is lola_total_time, Tara's time is tara_total_time.
    # The solution states "Because 200 < 220 Lola wins.", meaning Lola is faster, so Tara is slower.
    slower_time = max(lola_total_time, tara_total_time)

    # FA
    answer = slower_time
    return answer