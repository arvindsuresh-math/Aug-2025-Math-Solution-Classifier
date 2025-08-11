def solve():
    """Index: 1401.
    Returns: the number of laundry loads needed to clean all used towels.
    """
    # L1
    kylie_towels = 3 # Kylie uses 3 bath towels
    daughters_towels = 6 # her 2 daughters use a total of 6 bath towels
    husband_towels = 3 # her husband uses a total of 3 bath towels
    total_towels_used = kylie_towels + daughters_towels + husband_towels

    # L2
    washing_machine_capacity = 4 # washing machine can fit 4 bath towels
    num_laundry_loads = total_towels_used / washing_machine_capacity

    # FA
    answer = num_laundry_loads
    return answer