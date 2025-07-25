def solve():
    """Index: 2546.
    Returns: the total hours Jack spends making coffee over 24 days.
    """
    # L1
    batch_gallons = 1.5 # batches of 1.5 gallons
    ounces_per_gallon = 128 # WK
    batch_ounces = batch_gallons * ounces_per_gallon

    # L2
    drinks_per_2days = 96 # drinks 96 ounces every 2 days
    days_per_period = 2 # every 2 days
    drinks_per_day = drinks_per_2days / days_per_period

    # L3
    days_per_batch = batch_ounces / drinks_per_day

    # L4
    total_days = 24 # over 24 days
    num_batches = total_days / days_per_batch

    # L5
    hours_per_batch = 20 # takes 20 hours to make coffee
    total_hours = num_batches * hours_per_batch

    # FA
    answer = total_hours
    return answer