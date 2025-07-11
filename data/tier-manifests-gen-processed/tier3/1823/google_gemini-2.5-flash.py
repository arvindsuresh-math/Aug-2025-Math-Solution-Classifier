def solve():
    """Index: 1823.
    Returns: the total number of months Gerald spends in jail.
    """
    # L1
    years_sentence = 2 # 2 years for poisoning
    months_per_year = 12 # WK
    sentence_in_months = years_sentence * months_per_year

    # L2
    assault_months = 3 # 3 months for assault
    total_months_initial = sentence_in_months + assault_months

    # L3
    extension_divisor = 3 # extends his sentence by 1/3
    extension_months = total_months_initial / extension_divisor

    # L4
    total_sentence_length = total_months_initial + extension_months

    # FA
    answer = total_sentence_length
    return answer