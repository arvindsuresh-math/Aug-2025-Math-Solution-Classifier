def solve():
    """Index: 2502.
    Returns: the total hours of enjoyable gameplay James gets.
    """
    # L1
    base_gameplay_hours = 100 # promises 100 hours of gameplay
    boring_percent = 0.8 # 80% of that is boring grinding
    boring_hours = base_gameplay_hours * boring_percent

    # L2
    enjoyable_hours_base = base_gameplay_hours - boring_hours

    # L3
    expansion_enjoyable_hours = 30 # expansion does add another 30 hours of enjoyable gameplay
    total_enjoyable_hours = enjoyable_hours_base + expansion_enjoyable_hours

    # FA
    answer = total_enjoyable_hours
    return answer