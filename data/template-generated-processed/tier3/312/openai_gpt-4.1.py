def solve():
    """Index: 312.
    Returns: the number of emus in Farmer Brown's flock.
    """
    # L1
    heads_per_emu = 1 # Each emu has 1 head
    legs_per_emu = 2 # Each emu has 2 legs
    heads_and_legs_per_emu = heads_per_emu + legs_per_emu

    # L2
    total_heads_and_legs = 60 # flock has a total of 60 heads and legs
    emus_in_flock = total_heads_and_legs / heads_and_legs_per_emu

    # FA
    answer = emus_in_flock
    return answer