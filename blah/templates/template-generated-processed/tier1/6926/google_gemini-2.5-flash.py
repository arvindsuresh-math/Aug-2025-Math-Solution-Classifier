def solve():
    """Index: 6926.
    Returns: the number of turquoise beads in the necklace.
    """
    # L1
    amethyst_beads = 7 # seven amethyst beads
    multiplier_for_amber = 2 # twice as many amber beads
    amber_beads = amethyst_beads * multiplier_for_amber

    # L2
    total_beads = 40 # A 40-bead necklace
    turquoise_beads = total_beads - amethyst_beads - amber_beads

    # FA
    answer = turquoise_beads
    return answer