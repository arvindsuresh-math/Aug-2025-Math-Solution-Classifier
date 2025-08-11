def solve():
    """Index: 1249.
    Returns: the additional time needed to charge the cell phone to 100%.
    """
    # L1
    full_charge_percentage = 100 # to reach 100% charge
    current_charge_percentage = 25 # has reached a 25% charge
    charge_ratio = full_charge_percentage / current_charge_percentage

    # L2
    initial_charge_time = 45 # charged for 45 minutes
    total_charge_time_needed = initial_charge_time * charge_ratio

    # L3
    remaining_charge_time = total_charge_time_needed - initial_charge_time

    # FA
    answer = remaining_charge_time
    return answer