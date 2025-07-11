def solve():
    """Index: 2474.
    Returns: the total number of years in the burglar's sentence.
    """
    # L1
    goods_stolen = 40000 # $40,000 worth of goods
    base_sentence_per_amount = 5000 # 1 year of jail for every $5,000
    base_sentence_years = goods_stolen / base_sentence_per_amount

    # L2
    third_offense_increase_percent = 25 # 25% increase for third offense
    percent_factor = 0.01 # WK
    third_offense_increase_years = base_sentence_years * third_offense_increase_percent * percent_factor

    # L3
    resisting_arrest_years = 2 # 2 additional years for resisting arrest
    total_sentence_years = base_sentence_years + third_offense_increase_years + resisting_arrest_years

    # FA
    answer = total_sentence_years
    return answer