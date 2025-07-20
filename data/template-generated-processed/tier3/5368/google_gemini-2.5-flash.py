def solve():
    """Index: 5368.
    Returns: the total number of pieces of meat on each slice of pizza.
    """
    # L1
    pepperoni_pieces = 30 # 30 pieces of pepperoni
    ham_multiplier = 2 # twice as many pieces of ham
    ham_pieces = pepperoni_pieces * ham_multiplier

    # L2
    sausage_additional_pieces = 12 # 12 more pieces of sausage than pepperoni
    sausage_pieces = pepperoni_pieces + sausage_additional_pieces

    # L3
    total_slices = 6 # 6 slices of pizza
    pepperoni_per_slice = pepperoni_pieces / total_slices

    # L4
    ham_per_slice = ham_pieces / total_slices

    # L5
    sausage_per_slice = sausage_pieces / total_slices

    # L6
    total_meat_per_slice = pepperoni_per_slice + ham_per_slice + sausage_per_slice

    # FA
    answer = total_meat_per_slice
    return answer