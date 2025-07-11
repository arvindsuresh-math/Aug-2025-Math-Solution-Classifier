def solve():
    """Index: 1750.
    Returns: how many more dollars Alberto spent on his car than Samara.
    """
    # L1
    samara_oil = 25 # Samara spent $25 on oil
    samara_tires = 467 # $467 on tires
    samara_detailing = 79 # $79 on detailing
    samara_total = samara_oil + samara_tires + samara_detailing

    # L2
    alberto_engine = 2457 # Alberto spent $2457 on a new engine
    difference = alberto_engine - samara_total

    # L3
    answer = difference
    return answer