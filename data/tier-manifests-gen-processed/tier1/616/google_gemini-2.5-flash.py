def solve():
    """Index: 616.
    Returns: the total number of balloons Kris and her brother blew up.
    """
    # L1
    kris_balloons_per_minute = 2 # Kris can blow up a total of 2 balloon per minute
    total_time_minutes = 30 # She has 30 minutes
    kris_total_balloons = kris_balloons_per_minute * total_time_minutes

    # L2
    brother_speed_multiplier_initial = 2 # her brother works twice as fast
    first_phase_duration_minutes = 15 # After 15 minutes
    brother_speed_first_phase = kris_balloons_per_minute * brother_speed_multiplier_initial

    # L3
    brother_balloons_first_phase = brother_speed_first_phase * first_phase_duration_minutes

    # L4
    brother_speed_multiplier_second = 2 # brother doubles his speed
    second_phase_duration_minutes = 15 # remaining 15 minutes
    brother_speed_second_phase = brother_speed_first_phase * brother_speed_multiplier_second

    # L5
    brother_balloons_second_phase = brother_speed_second_phase * second_phase_duration_minutes

    # L6
    brother_total_balloons = brother_balloons_first_phase + brother_balloons_second_phase

    # L7
    total_balloons_both = kris_total_balloons + brother_total_balloons

    # FA
    answer = total_balloons_both
    return answer