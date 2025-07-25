def solve():
    """Index: 341.
    Returns: the number of dust particles on the porch before Samuel swept.
    """
    # L1
    dust_after_walk = 331 # 331 after he walked across it
    dust_left_by_shoes = 223 # his shoes left 223 dust particles behind
    dust_before_walk = dust_after_walk - dust_left_by_shoes

    # L2
    remaining_fraction_denominator = 10 # nine-tenths of the dust particles from it (meaning 1/10 remained)
    original_dust_particles = dust_before_walk * remaining_fraction_denominator

    # FA
    answer = original_dust_particles
    return answer