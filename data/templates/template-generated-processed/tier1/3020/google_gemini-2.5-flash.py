def solve():
    """Index: 3020.
    Returns: the total money Erica earned in the past four months including today.
    """
    # L1
    fish_kg_past_four_months = 80 # 80 kg of fish in the past four months
    price_per_kg = 20 # $20 per kg of fish
    earnings_past_four_months = fish_kg_past_four_months * price_per_kg

    # L2
    multiplier_today = 2 # twice as many fish
    fish_kg_today = fish_kg_past_four_months * multiplier_today

    # L3
    earnings_today = fish_kg_today * price_per_kg

    # L4
    total_earnings = earnings_today + earnings_past_four_months

    # FA
    answer = total_earnings
    return answer