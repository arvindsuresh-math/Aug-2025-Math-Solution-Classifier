def solve():
    """Index: 3195.
    Returns: the number of sodas James drinks per day.
    """
    # L1
    packs_bought = 5 # 5 packs of sodas
    sodas_per_pack = 12 # 12 sodas each
    sodas_bought = packs_bought * sodas_per_pack

    # L2
    sodas_already_had = 10 # He had 10 sodas already
    total_sodas = sodas_bought + sodas_already_had

    # L3
    days_in_week = 7 # He finishes all the sodas in 1 week
    sodas_per_day = total_sodas / days_in_week

    # FA
    answer = sodas_per_day
    return answer