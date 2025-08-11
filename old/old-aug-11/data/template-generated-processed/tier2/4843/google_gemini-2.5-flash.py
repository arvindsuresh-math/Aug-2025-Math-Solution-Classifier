def solve():
    """Index: 4843.
    Returns: the total hours Josh spends on extracurricular activities from Monday to Friday.
    """
    # L1
    soccer_daily_duration = 2 # from 3:00 p.m. to 5:00 p.m.
    soccer_days_per_week = 3 # Monday, Wednesday, and Friday
    total_soccer_hours = soccer_daily_duration * soccer_days_per_week

    # L2
    band_daily_duration = 1.5 # from 3:30 p.m. to 5:00 p.m.
    band_days_per_week = 2 # Tuesday and Thursday
    total_band_hours = band_daily_duration * band_days_per_week

    # L3
    total_extracurricular_hours = total_soccer_hours + total_band_hours

    # FA
    answer = total_extracurricular_hours
    return answer