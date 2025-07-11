def solve():
    """Index: 2192.
    Returns: the total money Suzanne's parents will donate for the race.
    """
    # L1
    initial_donation_per_km = 10 # $10 for her first kilometer
    doubling_factor = 2 # double the donation
    donation_km2 = initial_donation_per_km * doubling_factor

    # L2
    donation_km3 = donation_km2 * doubling_factor

    # L3
    donation_km4 = donation_km3 * doubling_factor

    # L4
    donation_km5 = donation_km4 * doubling_factor

    # L5
    total_donation = initial_donation_per_km + donation_km2 + donation_km3 + donation_km4 + donation_km5

    # FA
    answer = total_donation
    return answer