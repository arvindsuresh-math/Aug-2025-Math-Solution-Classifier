def solve():
    """Index: 643.
    Returns: how much farther, in feet, Velma's flashlight can be seen compared to Veronica's.
    """
    # L1
    veronica_distance = 1000 # a distance of 1000 feet
    freddie_multiplier = 3 # three times farther than Veronica's flashlight
    freddie_distance = freddie_multiplier * veronica_distance

    # L2
    velma_multiplier = 5 # 5 times farther than Freddie's flashlight
    five_times_freddie = velma_multiplier * freddie_distance

    # L3
    velma_less = 2000 # 2000 feet less than 5 times farther than Freddie's flashlight
    velma_distance = five_times_freddie - velma_less

    # L4
    farther_than_veronica = velma_distance - veronica_distance

    # FA
    answer = farther_than_veronica
    return answer