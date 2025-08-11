def solve():
    """Index: 7462.
    Returns: the number of gold bars each friend will receive.
    """
    # L1
    initial_gold_bars = 100 # 100 gold bars
    lost_gold_bars = 20 # 20 gold bars were lost
    remaining_gold_bars = initial_gold_bars - lost_gold_bars

    # L2
    num_friends = 4 # 4 friends
    gold_bars_per_friend = remaining_gold_bars / num_friends

    # FA
    answer = gold_bars_per_friend
    return answer