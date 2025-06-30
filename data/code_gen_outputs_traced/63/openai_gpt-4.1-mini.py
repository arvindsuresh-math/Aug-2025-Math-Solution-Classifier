def solve(
    goal_situps: int = 30,  # Shawna's workout goal is 30 situps
    monday_situps: int = 12,  # On Monday, Shawna was only able to do 12 situps
    tuesday_situps: int = 19  # On Tuesday, Shawna was only able to do 19 situps
):
    """Index: 63.
    Returns: the number of situps Shawna needs to do on Wednesday to meet her goal.
    """

    #: L1
    monday_shortfall = goal_situps - monday_situps # eval: 18 = 30 - 12

    #: L2
    tuesday_shortfall = goal_situps - tuesday_situps # eval: 11 = 30 - 19

    #: L3
    wednesday_situps_needed = goal_situps + monday_shortfall + tuesday_shortfall # eval: 59 = 30 + 18 + 11

    #: FA
    answer = wednesday_situps_needed # eval: 59 = 59
    return answer # eval: return 59
