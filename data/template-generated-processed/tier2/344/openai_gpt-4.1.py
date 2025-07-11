def solve():
    """Index: 344.
    Returns: the number of marbles Archie started with.
    """
    # L1
    marbles_left = 20 # he has 20 left
    sewer_loss_factor = 2 # loses half down a sewer
    before_sewer = marbles_left * sewer_loss_factor

    # L2
    percent_remaining = 0.4 # 60% lost, so 40% remain
    initial_marbles = before_sewer / percent_remaining

    # FA
    answer = initial_marbles
    return answer