def solve():
    """Index: 1616.
    Returns: the number of hours Tristan spends studying on Saturday.
    """
    # L1
    monday_study_hours = 4 # On Monday, he studies for 4 hours
    tuesday_multiplier = 2 # studies for twice this long on Tuesday
    tuesday_study_hours = monday_study_hours * tuesday_multiplier

    # L2
    midweek_daily_hours = 3 # On Wednesday, Thursday, and Friday he studies for 3 hours each day
    first_five_days_total = monday_study_hours + tuesday_study_hours + midweek_daily_hours + midweek_daily_hours + midweek_daily_hours

    # L3
    total_planned_hours = 25 # wants to study for a total of 25 hours over the week
    remaining_study_hours = total_planned_hours - first_five_days_total

    # L4
    weekend_days = 2 # divides the remaining amount of study time evenly between Saturday and Sunday
    saturday_study_hours = remaining_study_hours / weekend_days

    # FA
    answer = saturday_study_hours
    return answer