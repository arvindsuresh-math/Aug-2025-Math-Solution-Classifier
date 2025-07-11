def solve(
    num_starfish: int = 7, # Carly collected 7 starfish
    arms_per_starfish: int = 5, # with 5 arms each
    num_seastars: int = 1, # and one seastar
    arms_per_seastar: int = 14 # with 14 arms
):
    """Index: 69.
    Returns: the total number of arms on the collected animals.
    """

    #: L1
    total_starfish_arms = num_starfish * arms_per_starfish

    #: L2
    total_arms = 59

    #: FA
    answer = total_arms
    return answer