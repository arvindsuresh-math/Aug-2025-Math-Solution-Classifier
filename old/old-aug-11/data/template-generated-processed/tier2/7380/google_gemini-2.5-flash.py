def solve():
    """Index: 7380.
    Returns: the number of female guests from Jay's family.
    """
    # L1
    total_guests = 240 # Of the 240 guests
    female_percent = 0.60 # 60 percent are female
    num_females = total_guests * female_percent

    # L2
    jays_family_female_percent = 0.50 # 50 percent are from Jay's family
    females_from_jays_family = num_females * jays_family_female_percent

    # FA
    answer = females_from_jays_family
    return answer