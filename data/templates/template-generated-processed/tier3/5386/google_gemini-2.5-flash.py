def solve():
    """Index: 5386.
    Returns: the total number of trolls Erin counted.
    """
    # L1
    forest_trolls = 6 # six trolls hiding by the path
    four_times_factor = 4 # four times that number
    four_times_forest_trolls = forest_trolls * four_times_factor

    # L2
    subtraction_amount = 6 # 6 less than four times that number
    bridge_trolls = four_times_forest_trolls - subtraction_amount

    # L3
    division_factor = 2 # half as many trolls
    plains_trolls = bridge_trolls / division_factor

    # L4
    total_trolls = forest_trolls + bridge_trolls + plains_trolls

    # FA
    answer = total_trolls
    return answer