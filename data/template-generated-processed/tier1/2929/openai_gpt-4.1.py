def solve():
    """Index: 2929.
    Returns: the number of spelling badges Celestia has.
    """
    # L1
    hermione_badges = 14 # Hermione has 14
    luna_badges = 17 # Luna has 17
    hermione_luna_badges = hermione_badges + luna_badges

    # L2
    total_badges = 83 # combined have 83 spelling badges
    celestia_badges = total_badges - hermione_luna_badges

    # FA
    answer = celestia_badges
    return answer