def solve():
    """Index: 1168.
    Returns: the total number of tulips Arwen and Elrond picked.
    """
    # L1
    arwen_tulips = 20 # Arwen was able to get 20 tulips
    elrond_multiplier = 2 # Elrond was able to get twice as many tulips as Arwen did
    elrond_tulips = arwen_tulips * elrond_multiplier

    # L2
    total_tulips = elrond_tulips + arwen_tulips

    # FA
    answer = total_tulips
    return answer