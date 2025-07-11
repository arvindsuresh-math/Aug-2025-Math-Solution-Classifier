def solve():
    """Index: 2339.
    Returns: the total number of shirts Hazel and Razel have together.
    """
    # L1
    hazel_shirts = 6 # Hazel received 6 shirts
    razel_multiplier = 2 # Razel received twice the number of shirts as Hazel
    razel_shirts = hazel_shirts * razel_multiplier

    # L2
    total_shirts = razel_shirts + hazel_shirts

    # FA
    answer = total_shirts
    return answer