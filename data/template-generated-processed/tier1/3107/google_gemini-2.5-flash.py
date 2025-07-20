def solve():
    """Index: 3107.
    Returns: the total hours Cathy worked during the 2 months.
    """
    # L1
    weeks_per_month = 4 # four weeks in a month
    num_months = 2 # 2 months
    total_weeks_supposed_to_work = weeks_per_month * num_months

    # L2
    chris_sick_weeks = 1 # Chris got sick for one week
    chris_actual_weeks_worked = total_weeks_supposed_to_work - chris_sick_weeks
    cathy_total_weeks_worked = total_weeks_supposed_to_work + chris_sick_weeks

    # L3
    hours_per_week = 20 # 20 hours per week each
    cathy_total_hours_worked = cathy_total_weeks_worked * hours_per_week

    # FA
    answer = cathy_total_hours_worked
    return answer