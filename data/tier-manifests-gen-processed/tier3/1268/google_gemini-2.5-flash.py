def solve():
    """Index: 1268.
    Returns: the number of days it will take for the toothpaste to run out.
    """
    # L1
    anne_usage = 1 # Anne and her brother use 1 gram each
    brother_usage = 1 # Anne and her brother use 1 gram each
    anne_and_brother_total_usage = anne_usage + brother_usage

    # L2
    dad_usage = 3 # Anne's dad uses 3 grams at each brushing
    mom_usage = 2 # her mom uses 2 grams
    total_usage_per_brushing = dad_usage + mom_usage + anne_and_brother_total_usage

    # L3
    brushings_per_day = 3 # Each member of the family brushes their teeth three times a day
    daily_usage = total_usage_per_brushing * brushings_per_day

    # L4
    initial_toothpaste_grams = 105 # The toothpaste in Anne's family's bathroom contains 105 grams
    days_to_run_out = initial_toothpaste_grams / daily_usage

    # FA
    answer = days_to_run_out
    return answer