def solve():
    """Index: 7354.
    Returns: the total gallons of gas needed to cut the lawn.
    """
    # L1
    cuts_per_month_low_season = 2 # 2 times per month
    num_months_low_season = 4 # For March, April, September and October
    total_cuts_low_season = cuts_per_month_low_season * num_months_low_season

    # L2
    cuts_per_month_high_season = 4 # 4 times per month
    num_months_high_season = 4 # In May, June, July and August
    total_cuts_high_season = cuts_per_month_high_season * num_months_high_season

    # L3
    total_cuts_overall = total_cuts_low_season + total_cuts_high_season

    # L4
    frequency_for_gas = 4 # every 4th time she cuts her lawn
    num_fill_ups = total_cuts_overall / frequency_for_gas

    # L5
    gallons_per_fill_up = 2 # 2 gallons of gas
    total_gallons_needed = gallons_per_fill_up * num_fill_ups

    # FA
    answer = total_gallons_needed
    return answer