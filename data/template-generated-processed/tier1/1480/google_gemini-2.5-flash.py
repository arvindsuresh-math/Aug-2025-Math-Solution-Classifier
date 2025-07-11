def solve():
    """Index: 1480.
    Returns: the number of more scoops of ice cream Victoria has than Oli.
    """
    # L1
    oli_scoops = 4 # 4 scoops of ice cream
    multiplier = 2 # twice more scoops
    victoria_scoops = oli_scoops * multiplier

    # L2
    difference_scoops = victoria_scoops - oli_scoops

    # FA
    answer = difference_scoops
    return answer