def solve():
    """Index: 5279.
    Returns: the number of phones left in the factory.
    """
    # L1
    last_year_production = 5000 # Last year’s production was 5000 phones
    production_multiplier = 2 # makes twice as many phones
    current_year_production = last_year_production * production_multiplier

    # L2
    quarter_denominator = 4 # a quarter of this year’s production
    sold_phones = current_year_production / quarter_denominator

    # L3
    phones_left = current_year_production - sold_phones

    # FA
    answer = phones_left
    return answer