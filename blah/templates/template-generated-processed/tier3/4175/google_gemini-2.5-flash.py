def solve():
    """Index: 4175.
    Returns: the total number of snacks dropped by the vending machine.
    """
    # L1
    total_uses = 30 # If thirty people have used the vending machine once each
    fail_frequency_denominator = 6 # one in six times
    failed_drops = total_uses / fail_frequency_denominator

    # L2
    double_drop_frequency_denominator = 10 # One in ten times
    double_drops = total_uses / double_drop_frequency_denominator

    # L3
    normal_drops = total_uses - failed_drops - double_drops

    # L4
    snacks_per_double_drop = 2 # accidentally drop two snacks
    double_drops_times_two = double_drops * snacks_per_double_drop
    total_snacks_dropped = normal_drops + double_drops_times_two

    # FA
    answer = total_snacks_dropped
    return answer