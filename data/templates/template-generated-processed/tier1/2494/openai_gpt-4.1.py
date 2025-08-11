def solve():
    """Index: 2494.
    Returns: the number of rocks Conner must collect on day three to at least tie Sydney.
    """
    # L1
    sydney_day1 = 4 # Sydney collects 4 rocks on day one
    conner_day1_multiplier = 8 # Conner collects 8 times as many
    conner_day1 = conner_day1_multiplier * sydney_day1

    # L2
    sydney_day3_multiplier = 2 # Sydney collects twice as many as Conner did on the first day
    sydney_day3 = conner_day1 * sydney_day3_multiplier

    # L3
    sydney_start = 837 # Sydney has 837 rocks before they start
    sydney_day2 = 0 # Sydney rests on day two
    sydney_total = sydney_start + sydney_day2 + sydney_day1 + sydney_day3

    # L4
    conner_start = 723 # Conner has 723 rocks before they start
    conner_day2 = 123 # Conner collects 123 on day two
    conner_before_day3 = conner_start + conner_day1 + conner_day2

    # L5
    conner_needed_day3 = sydney_total - conner_before_day3

    # FA
    answer = conner_needed_day3
    return answer