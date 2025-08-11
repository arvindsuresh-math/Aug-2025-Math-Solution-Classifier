def solve():
    """Index: 5547.
    Returns: the number of apples left after the dog eats some.
    """
    # L1
    apples_on_tree = 5 # 5 apples are hanging on the tree
    apples_on_ground = 8 # 8 have fallen to the ground
    total_apples_initial = apples_on_tree + apples_on_ground

    # L2
    dog_eats = 3 # dog eats 3 of the apples
    apples_left = total_apples_initial - dog_eats

    # FA
    answer = apples_left
    return answer