def solve():
    """Index: 3468.
    Returns: Big Joe's height in feet.
    """
    # L1
    pepe_height_feet = 4.5 # Pepe is 4 feet six inches tall

    # L2
    frank_taller_than_pepe = 0.5 # half a foot taller than Pepe
    frank_height = pepe_height_feet + frank_taller_than_pepe

    # L3
    larry_taller_than_frank = 1 # one foot taller than Frank
    larry_height = frank_height + larry_taller_than_frank

    # L4
    ben_taller_than_larry = 1 # one foot taller than Larry
    ben_height = larry_height + ben_taller_than_larry

    # L5
    big_joe_taller_than_ben = 1 # one foot taller than Ben
    big_joe_height = ben_height + big_joe_taller_than_ben

    # FA
    answer = big_joe_height
    return answer