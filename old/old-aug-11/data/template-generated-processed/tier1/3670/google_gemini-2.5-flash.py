def solve():
    """Index: 3670.
    Returns: the number of pieces of chalk Erika and her siblings originally had.
    """
    # L1
    erika = 1 # Erika and her 3 siblings
    siblings = 3 # 3 siblings
    friends = 3 # Another 3 friends join them
    total_people = erika + siblings + friends

    # L2
    chalk_per_person = 3 # have 3 pieces each
    total_chalk_needed = total_people * chalk_per_person

    # L3
    mom_brought_chalk = 12 # mom brings out another 12 pieces of chalk
    chalk_before_mom = total_chalk_needed - mom_brought_chalk

    # L4
    erika_lost_chalk = 2 # Erika loses 2 pieces of chalk
    original_chalk = chalk_before_mom + erika_lost_chalk

    # FA
    answer = original_chalk
    return answer