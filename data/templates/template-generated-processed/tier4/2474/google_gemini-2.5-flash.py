def solve():
    """Index: 2474.
    Returns: the total years of the burglar's sentence.
    """
    # L1
    stolen_goods_value = 40000 # $40,000 worth of goods
    cost_per_year = 5000 # $5,000 of goods stolen
    base_sentence_years = stolen_goods_value / cost_per_year

    # L2
    third_offense_increase_percent_num = 25 # increased by 25%
    percent_factor = 0.01 # WK
    third_offense_increase_years = base_sentence_years * third_offense_increase_percent_num * percent_factor

    # L3
    resisting_arrest_years = 2 # 2 additional years for resisting arrest
    total_sentence_years = base_sentence_years + third_offense_increase_years + resisting_arrest_years

    # FA
    answer = total_sentence_years
    return answer