def solve():
    """Index: 3501.
    Returns: the number of spoons Chenny bought.
    """
    # L1
    num_plates = 9 # 9 plates
    cost_per_plate = 2 # $2 each
    cost_of_plates = cost_per_plate * num_plates

    # L2
    total_paid = 24 # paid a total of $24
    cost_of_spoons = total_paid - cost_of_plates

    # L3
    cost_per_spoon = 1.50 # $1.50 each
    num_spoons = cost_of_spoons / cost_per_spoon

    # FA
    answer = num_spoons
    return answer