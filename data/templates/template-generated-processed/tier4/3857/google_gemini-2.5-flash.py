def solve():
    """Index: 3857.
    Returns: the number of times the quarterback is sacked for a loss.
    """
    # L1
    total_steps_back = 80 # 80 times in a game
    no_pass_percent = 0.30 # 30 percent of the time he does not get a pass thrown
    no_pass_thrown_times = total_steps_back * no_pass_percent

    # L2
    sacked_divisor = 2 # Half of the times that he does not throw the ball he is sacked
    sacked_times = no_pass_thrown_times / sacked_divisor

    # FA
    answer = sacked_times
    return answer