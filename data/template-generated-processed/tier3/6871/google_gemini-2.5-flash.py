def solve():
    """Index: 6871.
    Returns: the total number of eggs John gets in a week.
    """
    # L1
    emus_per_pen = 6 # each pen has 6 emus
    num_pens = 4 # He has 4 pens
    total_emus = emus_per_pen * num_pens

    # L2
    female_emu_fraction_denominator = 2 # half the emu are females
    female_emus = total_emus / female_emu_fraction_denominator

    # L3
    days_per_week = 7 # a week
    total_eggs_per_week = female_emus * days_per_week

    # FA
    answer = total_eggs_per_week
    return answer