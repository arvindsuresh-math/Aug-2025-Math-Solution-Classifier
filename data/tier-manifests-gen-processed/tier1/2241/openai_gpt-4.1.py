def solve():
    """Index: 2241.
    Returns: the number of hours it will take Darrel to catch up to the coyote.
    """
    # L2
    darrel_speed = 30 # Darrel travels east at 30 miles per hour
    coyote_speed = 15 # coyote travels east at 15 miles per hour
    time_head_start = 1 # coyote left the prints 1 hour ago
    # L6
    x = (coyote_speed * time_head_start) / (darrel_speed - coyote_speed)
    # FA
    answer = x
    return answer