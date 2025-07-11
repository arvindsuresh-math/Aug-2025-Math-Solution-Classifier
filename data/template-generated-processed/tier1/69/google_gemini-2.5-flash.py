def solve():
    """Index: 69.
    Returns: the total number of arms of the collected animals.
    """
    # L1
    num_starfish = 7 # 7 starfish
    arms_per_starfish = 5 # 5 arms each
    total_starfish_arms = num_starfish * arms_per_starfish

    # L2
    seastar_arms = 14 # one seastar with 14 arms
    total_arms = total_starfish_arms + seastar_arms

    # FA
    answer = total_arms
    return answer