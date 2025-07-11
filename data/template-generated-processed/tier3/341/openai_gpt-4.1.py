def solve():
    """Index: 341.
    Returns: the number of dust particles on the porch before Samuel swept.
    """
    # L1
    after_walk_particles = 331 # there were 331 after he walked across it
    shoe_particles = 223 # his shoes left 223 dust particles behind
    before_walk_particles = after_walk_particles - shoe_particles

    # L2
    remaining_fraction_denominator = 10 # nine-tenths cleared, so 1/10 remain
    original_particles = before_walk_particles * remaining_fraction_denominator

    # FA
    answer = original_particles
    return answer