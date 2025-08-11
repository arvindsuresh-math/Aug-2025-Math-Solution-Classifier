def solve():
    """Index: 212.
    Returns: the number of hours per day Randy needs to practice to become an expert before age 20.
    """
    # L1
    target_age = 20 # before he is 20
    current_age = 12 # Randy just turned 12
    years_to_practice = target_age - current_age

    # L2
    total_hours_required = 10000 # 10,000-hour rule
    hours_per_year = total_hours_required / years_to_practice

    # L3
    weeks_per_year = 52 # 52 weeks in a year
    vacation_weeks = 2 # two weeks off for vacation each year
    practice_weeks = weeks_per_year - vacation_weeks

    # L4
    days_per_week = 5 # Monday - Friday
    practice_days_per_year = practice_weeks * days_per_week

    # L5
    hours_per_day = hours_per_year / practice_days_per_year

    # FA
    answer = hours_per_day
    return answer