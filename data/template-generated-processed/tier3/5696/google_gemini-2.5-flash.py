def solve():
    """Index: 5696.
    Returns: the number of days Georgina has had the parrot.
    """
    # L1
    total_phrases_known = 17 # seventeen phrases
    initial_phrases = 3 # it already knew three phrases when she bought it
    phrases_learned_from_georgina = total_phrases_known - initial_phrases

    # L2
    phrases_per_week = 2 # two phrases a week
    weeks_georgina_had_parrot = phrases_learned_from_georgina / phrases_per_week

    # L3
    days_per_week = 7 # WK
    total_days_had_parrot = weeks_georgina_had_parrot * days_per_week

    # FA
    answer = total_days_had_parrot
    return answer