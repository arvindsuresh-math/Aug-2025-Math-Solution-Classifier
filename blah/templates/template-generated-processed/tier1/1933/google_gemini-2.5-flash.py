def solve():
    """Index: 1933.
    Returns: the cost Wendy paid for the tooth extraction.
    """
    # L1
    bill_multiplier = 5 # five times the cost of a filling
    cost_filling = 120 # $120 for a filling
    total_bill = bill_multiplier * cost_filling

    # L2
    num_fillings = 2 # two fillings
    cost_of_fillings = num_fillings * cost_filling

    # L3
    cost_cleaning = 70 # $70 for a cleaning
    cost_extraction = total_bill - cost_of_fillings - cost_cleaning

    # FA
    answer = cost_extraction
    return answer