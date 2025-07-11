def solve():
    """Index: 2086.
    Returns: the total cost in dollars to fill all displays.
    """
    # L1
    necklace_capacity = 12 # The necklace stand, which can hold 12 necklaces
    necklaces_current = 5 # currently holds 5 necklaces
    necklaces_needed = necklace_capacity - necklaces_current

    # L2
    cost_per_necklace = 4 # $4 per necklace
    cost_necklaces = necklaces_needed * cost_per_necklace

    # L3
    ring_capacity = 30 # The ring display, which can hold 30 rings
    rings_current = 18 # currently holds 18 rings
    rings_needed = ring_capacity - rings_current

    # L4
    cost_per_ring = 10 # $10 per ring
    cost_rings = rings_needed * cost_per_ring

    # L5
    bracelet_capacity = 15 # The bracelet display, which can hold 15 bracelets
    bracelets_current = 8 # currently holds 8 bracelets
    bracelets_needed = bracelet_capacity - bracelets_current

    # L6
    cost_per_bracelet = 5 # $5 per bracelet
    cost_bracelets = bracelets_needed * cost_per_bracelet

    # L7
    total_cost = cost_necklaces + cost_rings + cost_bracelets

    # FA
    answer = total_cost
    return answer