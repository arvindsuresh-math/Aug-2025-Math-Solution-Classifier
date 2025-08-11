def solve():
    """Index: 6114.
    Returns: the total number of individual shoes Nancy has.
    """
    # L1
    num_boots_pairs = 6 # six pairs of boots
    slippers_more_than_boots = 9 # nine more pairs of slippers than boots
    num_slippers_pairs = num_boots_pairs + slippers_more_than_boots

    # L2
    combined_slippers_boots_pairs = num_slippers_pairs + num_boots_pairs

    # L3
    heels_multiplier = 3 # three times the combined number of slippers and boots
    num_heels_pairs = combined_slippers_boots_pairs * heels_multiplier

    # L4
    total_pairs = num_slippers_pairs + num_boots_pairs + num_heels_pairs

    # L5
    shoes_per_pair = 2 # WK
    total_individual_shoes = total_pairs * shoes_per_pair

    # FA
    answer = total_individual_shoes
    return answer