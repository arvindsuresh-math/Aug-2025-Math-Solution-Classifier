def solve():
    """Index: 1728.
    Returns: Jana's height in inches.
    """
    # L1
    jess_height = 72 # Jess is 72 inches tall
    kelly_shorter_than_jess = 3 # Kelly is 3 inches shorter than Jess
    kelly_height = jess_height - kelly_shorter_than_jess

    # L2
    jana_taller_than_kelly = 5 # Jana is 5 inches taller than Kelly
    jana_height = kelly_height + jana_taller_than_kelly

    # FA
    answer = jana_height
    return answer