def solve():
    """Index: 976.
    Returns: Ludwig's total weekly salary.
    """
    # L1
    daily_salary = 10 # daily salary is $10
    full_work_days = 4 # Monday to Thursday
    earnings_mon_thu = daily_salary * full_work_days

    # L2
    half_day_divisor = 2 # half of the day
    half_day_salary = daily_salary / half_day_divisor

    # L3
    half_work_days = 3 # Friday, Saturday, and Sunday
    earnings_fri_sun = half_day_salary * half_work_days

    # L4
    total_weekly_salary = earnings_mon_thu + earnings_fri_sun

    # FA
    answer = total_weekly_salary
    return answer