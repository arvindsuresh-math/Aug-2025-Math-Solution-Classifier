def solve():
    """Index: 2511.
    Returns: the total length of time James might spend in jail.
    """
    # L1
    arson_sentence_per_count = 6 # each carry a 6-year sentence
    arson_counts = 2 # two count of arson
    total_arson_sentence = arson_sentence_per_count * arson_counts

    # L2
    explosives_multiplier = 2 # twice as long as the total arson sentence
    total_explosives_sentence = total_arson_sentence * explosives_multiplier

    # L3
    domestic_terrorism_sentence = 20 # 20 years
    total_jail_time = total_arson_sentence + total_explosives_sentence + domestic_terrorism_sentence

    # FA
    answer = total_jail_time
    return answer