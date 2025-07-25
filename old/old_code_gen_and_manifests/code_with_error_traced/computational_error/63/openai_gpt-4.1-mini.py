def solve(
    goal_situps: int = 30,  # Shawna's workout goal is 30 situps
    monday_situps: int = 12,  # On Monday, Shawna was only able to do 12 situps
    tuesday_situps: int = 19  # On Tuesday, Shawna was only able to do 19 situps
):
    """Index: 63.
    Returns: the number of situps Shawna needs to do on Wednesday to meet her goal.
    """

    #: L1
    monday_shortfall = 19 # eval: 19 = 19

    #: L2
    tuesday_shortfall = goal_situps - tuesday_situps # eval: 11 = 30 - 19

    #: L3
    wednesday_situps_needed = goal_situps + monday_shortfall + tuesday_shortfall # eval: 60 = 30 + 19 + 11

    #: FA
    answer = wednesday_situps_needed
    return answer # eval: return 60
