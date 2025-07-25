def solve():
    """Index: 6421.
    Returns: the total combined number of grapes in all three bowls.
    """
    # L1
    rob_grapes = 25 # Rob's bowl contained 25 grapes
    allie_more_than_rob = 2 # two more grapes than Rob's bowl
    allie_grapes = rob_grapes + allie_more_than_rob

    # L2
    allyn_more_than_allie = 4 # four more grapes than Allie's bowl
    allyn_grapes = allie_grapes + allyn_more_than_allie

    # L3
    total_grapes = rob_grapes + allie_grapes + allyn_grapes

    # FA
    answer = total_grapes
    return answer