def solve(
        workout_goal: int = 30, # Shawna's workout goal is 30 situps
        situps_monday: int = 12, # On Monday, Shawna was only able to do 12 situps
        situps_tuesday: int = 19 # she was only able to do 19 situps on Tuesday
    ):
    """Index: 63.
    Returns: the number of situps Shawna needs to do on Wednesday to meet her goal and make up for previous shortfalls.
    """

    #: L1
    shortfall_monday = 8 # eval: 8 = 8

    #: L2
    shortfall_tuesday = workout_goal - situps_tuesday # eval: 11 = 30 - 19

    #: L3
    situps_wednesday_needed = workout_goal + shortfall_monday + shortfall_tuesday # eval: 49 = 30 + 8 + 11

    #: FA
    answer = situps_wednesday_needed
    return answer # eval: return 49
