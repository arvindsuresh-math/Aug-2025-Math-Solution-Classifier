def solve():
    """Index: 2209.
    Returns: the total number of fish at the aquarium.
    """
    # L1
    stingrays = 28 # there are 28 stingrays
    sharks_per_stingray = 2 # twice as many sharks as stingrays
    sharks = sharks_per_stingray * stingrays

    # L2
    total_fish = sharks + stingrays

    # FA
    answer = total_fish
    return answer