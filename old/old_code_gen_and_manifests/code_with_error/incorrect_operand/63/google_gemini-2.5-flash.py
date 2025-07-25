def solve(
        workout_goal: int = 30, # Shawna's workout goal is 30 situps
        situps_monday: int = 12, # On Monday, Shawna was only able to do 12 situps
        situps_tuesday: int = 19 # she was only able to do 19 situps on Tuesday
    ):
    """Index: 63.
    Returns: the number of situps Shawna needs to do on Wednesday to meet her goal and make up for previous shortfalls.
    """

    #: L1
    shortfall_monday = situps_monday - situps_monday

    #: L2
    shortfall_tuesday = workout_goal - situps_tuesday

    #: L3
    situps_wednesday_needed = workout_goal + shortfall_monday + shortfall_tuesday

    #: FA
    answer = situps_wednesday_needed
    return answer