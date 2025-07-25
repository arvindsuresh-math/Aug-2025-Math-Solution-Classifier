def solve():
    """Index: 4506.
    Returns: the total number of months Jean is facing in jail.
    """
    # L1
    burglary_sentence_months = 18 # each burglary charge is 18 months
    burglary_charges = 2 # 2 burglary charges
    total_burglary_time = burglary_sentence_months * burglary_charges

    # L2
    arson_counts = 3 # 3 counts of arson
    arson_sentence_months = 36 # each arson count has a 36-month sentence
    total_arson_time = arson_counts * arson_sentence_months

    # L3
    petty_larceny_sentence_divisor = 3 # 1/3rd as long as a burglary charge
    larceny_sentence_months = burglary_sentence_months / petty_larceny_sentence_divisor

    # L4
    petty_larceny_multiplier = 6 # six times as many petty larceny as burglary charges
    total_larceny_charges = burglary_charges * petty_larceny_multiplier

    # L5
    total_larceny_time = larceny_sentence_months * total_larceny_charges

    # L6
    total_jail_time = total_burglary_time + total_larceny_time + total_arson_time

    # FA
    answer = total_jail_time
    return answer