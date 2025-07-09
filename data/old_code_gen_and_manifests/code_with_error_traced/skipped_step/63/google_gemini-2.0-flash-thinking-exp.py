def solve(
    goal_situps: int = 30, # Shawna's workout goal is 30 situps
    situps_monday: int = 12, # On Monday, Shawna was only able to do 12 situps
    situps_tuesday: int = 19 # she was only able to do 19 situps on Tuesday
):
    """Index: 63.
    Returns: the number of situps Shawna needs to do on Wednesday."""

    #: L1
    deficit_monday = goal_situps - situps_monday # eval: 18 = 30 - 12

    #: L2
    deficit_tuesday = goal_situps - situps_tuesday # eval: 11 = 30 - 19

    #: L3

    #: FA
    answer = situps_tuesday
    return answer # eval: return 19
