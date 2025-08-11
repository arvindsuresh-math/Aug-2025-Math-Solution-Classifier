def solve():
    """Index: 3960.
    Returns: how much Leila earns per week.
    """
    # L1
    voltaire_viewers_per_day = 50 # Voltaire has an average of 50 viewers per day
    leila_multiplier = 2 # twice the number of viewers Voltaire has
    leila_viewers_per_day = voltaire_viewers_per_day * leila_multiplier

    # L2
    earnings_per_view = 0.50 # earn $0.50 per view
    leila_earnings_per_day = leila_viewers_per_day * earnings_per_view

    # L3
    days_per_week = 7 # WK
    leila_earnings_per_week = leila_earnings_per_day * days_per_week

    # FA
    answer = leila_earnings_per_week
    return answer