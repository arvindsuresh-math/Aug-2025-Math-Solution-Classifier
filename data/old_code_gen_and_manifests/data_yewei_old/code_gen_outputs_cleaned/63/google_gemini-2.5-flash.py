def solve():
    # Shawna's daily situps goal
    daily_goal = 30

    # Situps done on Monday
    situps_monday = 12

    # Situps done on Tuesday
    situps_tuesday = 19

    # Calculate situps short on Monday
    short_monday = daily_goal - situps_monday

    # Calculate situps short on Tuesday
    short_tuesday = daily_goal - situps_tuesday

    # Calculate total situps needed on Wednesday
    # This includes Wednesday's daily goal plus the situps missed on Monday and Tuesday
    situps_wednesday_needed = daily_goal + short_monday + short_tuesday

    return situps_wednesday_needed

# Execute the function to get the answer
answer = solve()