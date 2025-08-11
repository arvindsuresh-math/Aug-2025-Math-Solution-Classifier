def solve():
    """Index: 3576.
    Returns: the time in seconds it took Billy to swim his final lap.
    """
    # L1
    margaret_total_minutes = 10 # Margaret finishes swimming all of her laps in 10 minutes
    seconds_per_minute = 60 # WK
    margaret_total_seconds = margaret_total_minutes * seconds_per_minute

    # L2
    billy_first_5_laps_minutes = 2 # Billy swims his first 5 laps in 2 minutes
    billy_first_5_laps_seconds = billy_first_5_laps_minutes * seconds_per_minute

    # L3
    billy_next_3_laps_minutes = 4 # swims the next 3 laps in 4 minutes
    billy_next_3_laps_seconds = billy_next_3_laps_minutes * seconds_per_minute

    # L4
    billy_ninth_lap_minutes = 1 # swims the next lap in 1 minute
    billy_ninth_lap_seconds = billy_ninth_lap_minutes * seconds_per_minute

    # L5
    billy_first_9_laps_total_seconds = billy_first_5_laps_seconds + billy_next_3_laps_seconds + billy_ninth_lap_seconds

    # L6
    billy_wins_by_seconds = 30 # Billy wins the competition by finishing his laps 30 seconds before Margaret does
    billy_total_time_seconds = margaret_total_seconds - billy_wins_by_seconds

    # L7
    billy_final_lap_time_seconds = billy_total_time_seconds - billy_first_9_laps_total_seconds

    # FA
    answer = billy_final_lap_time_seconds
    return answer