def solve(
        num_starfish: int = 7, # Carly collected 7 starfish
        arms_per_starfish: int = 5, # 5 arms each
        arms_seastar: int = 14 # one seastar with 14 arms
    ):
    """Index: 69.
    Returns: the total number of arms the collected animals have.
    """

    #: L1
    total_starfish_arms = arms_per_starfish * arms_per_starfish

    #: L2
    total_arms = total_starfish_arms + arms_seastar

    #: FA
    answer = total_arms
    return answer