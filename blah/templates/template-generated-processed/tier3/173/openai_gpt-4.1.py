def solve():
    """Index: 173.
    Returns: the number of seconds of head start the turtle needs to tie with the hare in a 20-foot race.
    """
    # L1
    race_distance = 20 # 20 foot-race
    hare_speed = 10 # hare runs 10 feet/second
    hare_time = race_distance / hare_speed

    # L2
    turtle_speed = 1 # turtle crawls 1 foot/second
    turtle_time = race_distance / turtle_speed

    # L3
    head_start = turtle_time - hare_time

    # FA
    answer = head_start
    return answer