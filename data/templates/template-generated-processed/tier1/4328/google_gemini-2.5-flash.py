def solve():
    """Index: 4328.
    Returns: the total amount the fisherman earns every day.
    """
    # L1
    red_snappers_per_day = 8 # 8 Red snappers
    red_snapper_cost = 3 # $3
    earnings_red_snappers = red_snapper_cost * red_snappers_per_day

    # L2
    tuna_cost = 2 # $2
    tunas_per_day = 14 # 14 Tunas
    earnings_tunas = tuna_cost * tunas_per_day

    # L3
    total_earnings = earnings_red_snappers + earnings_tunas

    # FA
    answer = total_earnings
    return answer