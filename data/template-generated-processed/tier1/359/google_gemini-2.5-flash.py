def solve():
    """Index: 359.
    Returns: the total number of pages finished by Rene, Lulu, and Cherry.
    """
    # Intermediate calculation for the time multiplier, derived from question inputs.
    initial_time_unit_minutes = 60 # 60 minutes
    total_reading_minutes = 240 # reading for 240 minutes
    time_multiplier = total_reading_minutes / initial_time_unit_minutes

    # L1
    rene_pages_per_60_min = 30 # 30 pages in 60 minutes
    rene_total_pages = rene_pages_per_60_min * time_multiplier

    # L2
    lulu_pages_per_60_min = 27 # 27 pages in 60 minutes
    lulu_total_pages = lulu_pages_per_60_min * time_multiplier

    # L3
    cherry_pages_per_60_min = 25 # 25 pages in 60 minutes
    cherry_total_pages = cherry_pages_per_60_min * time_multiplier

    # L4
    total_pages_finished = rene_total_pages + lulu_total_pages + cherry_total_pages

    # FA
    answer = total_pages_finished
    return answer