def solve():
    """Index: 2511.
    Returns: the total number of years James might spend in jail.
    """
    # L1
    arson_years_per_count = 6 # arson counts each carry a 6-year sentence
    arson_counts = 2 # two count of arson
    total_arson_years = arson_years_per_count * arson_counts

    # L2
    explosives_multiplier = 2 # explosives sentence is twice as long as the total arson sentence
    explosives_years = total_arson_years * explosives_multiplier

    # L3
    domestic_terrorism_years = 20 # domestic terrorism charge's sentence is 20 years
    total_sentence_years = total_arson_years + explosives_years + domestic_terrorism_years

    # FA
    answer = total_sentence_years
    return answer