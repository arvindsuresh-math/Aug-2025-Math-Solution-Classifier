def solve():
    """Index: 1933.
    Returns: the amount Wendy paid for the tooth extraction.
    """
    # L1
    num_fillings_in_bill = 5 # bill was five times the cost of a filling
    cost_per_filling = 120 # $120 for a filling
    total_bill = num_fillings_in_bill * cost_per_filling

    # L2
    num_fillings = 2 # two fillings
    fillings_cost = num_fillings * cost_per_filling

    # L3
    cleaning_cost = 70 # $70 for a cleaning
    extraction_cost = total_bill - fillings_cost - cleaning_cost

    # FA
    answer = extraction_cost
    return answer