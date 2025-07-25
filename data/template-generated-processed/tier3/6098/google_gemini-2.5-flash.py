def solve():
    """Index: 6098.
    Returns: the total number of steps Tom will have gone up.
    """
    # L1
    total_steps_matt_reached = 220 # Matt has reached 220 steps above the entrance
    matt_steps_per_minute = 20 # Matt goes up the stairs 20 steps per minute
    time_taken_minutes = total_steps_matt_reached / matt_steps_per_minute

    # L2
    tom_extra_steps_per_minute = 5 # Tom goes up the stairs 5 steps per minute more than Matt
    tom_extra_steps_total = time_taken_minutes * tom_extra_steps_per_minute

    # L3
    total_steps_tom_climbed = total_steps_matt_reached + tom_extra_steps_total

    # FA
    answer = total_steps_tom_climbed
    return answer