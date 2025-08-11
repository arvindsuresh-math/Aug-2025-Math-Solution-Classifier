def solve():
    """Index: 4823.
    Returns: the total number of fires put out by Doug, Kai, and Eli.
    """
    # L1
    doug_fires = 20 # Doug has put out 20 fires
    kai_multiplier = 3 # 3 times more than Doug
    kai_fires = doug_fires * kai_multiplier

    # L2
    eli_divisor = 2 # half the number of fires Kai was able to
    eli_fires = kai_fires / eli_divisor

    # L3
    total_fires = doug_fires + kai_fires + eli_fires

    # FA
    answer = total_fires
    return answer