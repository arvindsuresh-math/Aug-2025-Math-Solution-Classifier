def solve():
    """Index: 98.
    Returns: the total number of gumballs Hector originally purchased.
    """
    # L1
    todd_gumballs = 4 # gave 4 to Todd
    alisha_multiplier = 2 # twice as many as he had given Todd
    alisha_gumballs = todd_gumballs * alisha_multiplier

    # L2
    bobby_multiplier = 4 # four times as many to Bobby as he had given to Alisha
    bobby_less = 5 # 5 less than four times as many
    bobby_gumballs = (alisha_gumballs * bobby_multiplier) - bobby_less

    # L3
    remaining_gumballs = 6 # had 6 gumballs remaining
    total_gumballs = todd_gumballs + alisha_gumballs + bobby_gumballs + remaining_gumballs

    # FA
    answer = total_gumballs
    return answer