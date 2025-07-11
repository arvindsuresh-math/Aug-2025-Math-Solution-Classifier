def solve():
    """Index: 1480.
    Returns: how many more scoops of ice cream Victoria has than Oli.
    """
    # L1
    oli_scoops = 4 # Oli's banana split has 4 scoops of ice cream
    victoria_multiplier = 2 # Victoria has twice more scoops
    victoria_scoops = oli_scoops * victoria_multiplier

    # L2
    victoria_more_than_oli = victoria_scoops - oli_scoops

    # FA
    answer = victoria_more_than_oli
    return answer