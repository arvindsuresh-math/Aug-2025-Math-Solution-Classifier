def solve():
    """Index: 3091.
    Returns: the total number of sodas Marcy will have for the party.
    """
    # L1
    sodas_marcy_had_initial = 22 # 22 sodas in her fridge
    multiplier_two_times = 2 # two times the number of sodas
    two_times_sodas_marcy = sodas_marcy_had_initial * multiplier_two_times

    # L2
    tina_gave_base = 12 # gave her 12
    sodas_tina_gave = two_times_sodas_marcy + tina_gave_base

    # L3
    total_sodas = sodas_marcy_had_initial + sodas_tina_gave

    # FA
    answer = total_sodas
    return answer