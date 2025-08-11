def solve():
    """Index: 4745.
    Returns: the number of stickers Jerry has.
    """
    # L1
    Fred_stickers = 18 # Fred has 18 stickers
    george_fewer_than_fred = 6 # George has 6 fewer stickers than his brother Fred
    george_stickers = Fred_stickers - george_fewer_than_fred

    # L2
    jerry_times_george = 3 # Jerry has three times as many stickers as George
    jerry_stickers = george_stickers * jerry_times_george

    # FA
    answer = jerry_stickers
    return answer