def solve():
    """Index: 0.
    Returns: the total number of clips Natalia sold in April and May.
    """
    # L1
    april_clips = 48 # 48 of her friends in April
    may_divisor = 2 # half as many clips in May
    may_clips = april_clips / may_divisor

    # L2
    total_clips = april_clips + may_clips

    # FA
    answer = total_clips
    return answer