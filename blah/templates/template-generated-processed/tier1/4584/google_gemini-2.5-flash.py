def solve():
    """Index: 4584.
    Returns: the total number of fish caught by Keith and Blaine.
    """
    # L1
    blaine_fish = 5 # Blaine caught 5 fish
    multiplier_keith = 2 # twice as many as Blaine's
    keith_fish = blaine_fish * multiplier_keith

    # L2
    total_fish = blaine_fish + keith_fish

    # FA
    answer = total_fish
    return answer