def solve():
    """Index: 6452.
    Returns: the total number of stickers Elizabeth uses.
    """
    # L1
    initial_bottles = 10 # Elizabeth has 10 reusable water bottles
    lost_at_school = 2 # loses 2 water bottles at school
    stolen_at_dance = 1 # steals 1 of her water bottles at dance practice
    remaining_bottles = initial_bottles - lost_at_school - stolen_at_dance

    # L2
    stickers_per_bottle = 3 # places 3 stickers on each of her remaining bottles
    total_stickers = remaining_bottles * stickers_per_bottle

    # FA
    answer = total_stickers
    return answer