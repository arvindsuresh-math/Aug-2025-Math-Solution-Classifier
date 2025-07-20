def solve():
    """Index: 5063.
    Returns: the total number of packs of notebook paper Chip will use.
    """
    # L1
    pages_per_day_per_class = 2 # 2 pages of notes every day
    num_classes = 5 # 5 classes
    pages_per_day_total = pages_per_day_per_class * num_classes

    # L2
    days_per_week = 5 # 5 days a week
    pages_per_week = pages_per_day_total * days_per_week

    # L3
    num_weeks = 6 # After 6 weeks
    total_pages_notes = pages_per_week * num_weeks

    # L4
    pages_per_pack = 100 # 100 sheets of paper per pack
    packs_used = total_pages_notes / pages_per_pack

    # FA
    answer = packs_used
    return answer