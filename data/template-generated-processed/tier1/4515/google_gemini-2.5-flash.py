def solve():
    """Index: 4515.
    Returns: the total earnings for three days.
    """
    # L1
    kilos_two_days_ago = 5 # 5 kilos of laundries
    more_than_previous_day = 5 # five kilos of laundries more than the previous day
    kilos_yesterday = kilos_two_days_ago + more_than_previous_day

    # L2
    multiplier_today = 2 # twice the number of kilos than yesterday
    kilos_today = multiplier_today * kilos_yesterday

    # L3
    total_kilos_three_days = kilos_two_days_ago + kilos_yesterday + kilos_today

    # L4
    charge_per_kilo = 2 # $2 per kilo of laundry
    total_earnings = total_kilos_three_days * charge_per_kilo

    # FA
    answer = total_earnings
    return answer