def solve(
    num_starfish: int = 7,  # Carly collected 7 starfish
    arms_per_starfish: int = 5,  # with 5 arms each
    num_seastar: int = 1,  # and one seastar
    arms_per_seastar: int = 14  # with 14 arms
):
    """Index: 69.
    Returns: the total number of arms of the collected animals."""

    #: L1
    total_starfish_arms = num_starfish * arms_per_starfish

    #: L2
    total_arms = total_starfish_arms + arms_per_seastar

    answer = total_arms  # FINAL ANSWER
    return answer