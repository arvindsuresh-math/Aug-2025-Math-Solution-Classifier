def solve():
    """Index: 2502.
    Returns: the total enjoyable gameplay hours James gets.
    """
    # L1
    total_gameplay_hours = 100 # 100 hours of gameplay
    boring_grinding_percent = 0.8 # 80% of that is boring grinding
    grinding_hours = total_gameplay_hours * boring_grinding_percent

    # L2
    initial_enjoyable_gameplay = total_gameplay_hours - grinding_hours

    # L3
    expansion_enjoyable_hours = 30 # another 30 hours of enjoyable gameplay
    total_enjoyable_gameplay = initial_enjoyable_gameplay + expansion_enjoyable_hours

    # FA
    answer = total_enjoyable_gameplay
    return answer