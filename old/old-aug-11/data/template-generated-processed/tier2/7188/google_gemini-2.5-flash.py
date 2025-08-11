def solve():
    """Index: 7188.
    Returns: how much Shem earns for an 8-hour workday.
    """
    # L1
    kem_hourly_wage = 4 # Kem earns $4 per hour
    shem_wage_multiplier = 2.5 # Shem makes 2.5 times more money per hour than Kem
    shem_hourly_wage = kem_hourly_wage * shem_wage_multiplier

    # L2
    workday_hours = 8 # for an 8-hour workday
    shem_daily_wage = shem_hourly_wage * workday_hours

    # FA
    answer = shem_daily_wage
    return answer