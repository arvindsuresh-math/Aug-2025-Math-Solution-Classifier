def solve():
    """Index: 3698.
    Returns: the total number of pets the three have together.
    """
    # L1
    elodie_rats = 30 # Elodie has 30 rats
    hunter_less_than_elodie = 10 # 10 rats more than Hunter
    hunter_rats = elodie_rats - hunter_less_than_elodie

    # L2
    elodie_hunter_total = hunter_rats + elodie_rats

    # L3
    kenia_multiplier = 3 # three times as many rats
    kenia_rats = kenia_multiplier * elodie_hunter_total

    # L4
    total_pets = kenia_rats + elodie_hunter_total

    # FA
    answer = total_pets
    return answer