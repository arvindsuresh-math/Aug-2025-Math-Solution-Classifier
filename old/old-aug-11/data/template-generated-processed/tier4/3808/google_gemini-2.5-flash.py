from fractions import Fraction

def solve():
    """Index: 3808.
    Returns: the total number of people in the band.
    """
    # L1
    initial_flutes = 20 # 20 flutes
    flute_acceptance_rate = 0.8 # 80% of the 20 flutes got in
    accepted_flutes = initial_flutes * flute_acceptance_rate

    # L2
    initial_clarinets = 30 # 30 clarinets
    clarinet_acceptance_rate = 0.5 # half the 30 clarinets got in
    accepted_clarinets = initial_clarinets * clarinet_acceptance_rate

    # L3
    initial_trumpets = 60 # 60 trumpets
    trumpet_acceptance_fraction = Fraction(1, 3) # 1/3 of the 60 trumpets got in
    accepted_trumpets = initial_trumpets * trumpet_acceptance_fraction

    # L4
    initial_pianists = 20 # 20 pianists
    pianist_acceptance_fraction = Fraction(1, 10) # 1/10th of the 20 pianists got in
    accepted_pianists = initial_pianists * pianist_acceptance_fraction

    # L5
    total_band_members = accepted_flutes + accepted_clarinets + accepted_trumpets + accepted_pianists

    # FA
    answer = total_band_members
    return answer