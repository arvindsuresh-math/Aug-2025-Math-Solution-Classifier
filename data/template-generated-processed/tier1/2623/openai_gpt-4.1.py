def solve():
    """Index: 2623.
    Returns: the number of additional blue tickets Tom needs to win a new Bible.
    """
    # L1
    blue_per_red = 10 # each red ticket is obtained by trading in 10 blue tickets
    red_per_yellow = 10 # each yellow ticket is obtained by trading in 10 red tickets
    blue_per_yellow = blue_per_red * red_per_yellow

    # L2
    yellow_needed = 10 # win 10 yellow tickets to win a Bible
    blue_needed = yellow_needed * blue_per_yellow

    # L3
    tom_yellow = 8 # Tom has 8 yellow tickets
    blue_from_yellow = tom_yellow * blue_per_yellow

    # L4
    tom_red = 3 # Tom has 3 red tickets
    blue_from_red = tom_red * blue_per_red

    # L5
    tom_blue = 7 # Tom has 7 blue tickets
    tom_total_blue = blue_from_yellow + blue_from_red + tom_blue

    # L6
    blue_needed_more = blue_needed - tom_total_blue

    # FA
    answer = blue_needed_more
    return answer