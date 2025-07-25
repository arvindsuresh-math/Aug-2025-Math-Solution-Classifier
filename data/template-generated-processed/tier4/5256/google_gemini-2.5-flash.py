def solve():
    """Index: 5256.
    Returns: the number of paper cranes Alice still needs to fold.
    """
    # L1
    total_cranes = 1000 # Alice wants 1000 folded paper cranes
    alice_folds_fraction = 0.5 # She folds half by herself
    alice_folded = total_cranes * alice_folds_fraction

    # L2
    remaining_after_alice = total_cranes - alice_folded

    # L3
    friend_folds_divisor = 5 # a friend folds a fifth of the remaining paper cranes
    friend_folded = remaining_after_alice / friend_folds_divisor

    # L4
    cranes_alice_still_needs = total_cranes - alice_folded - friend_folded

    # FA
    answer = cranes_alice_still_needs
    return answer