def solve():
    """Index: 5710.
    Returns: the number of months Peter needs to wait.
    """
    # L1
    total_needed = 5000 # needs $5,000 to cover all the spending
    current_savings = 2900 # has $2,900 in savings right now
    remaining_needed = total_needed - current_savings

    # L2
    monthly_savings = 700 # save up $700 each month
    months_to_wait = remaining_needed / monthly_savings

    # FA
    answer = months_to_wait
    return answer