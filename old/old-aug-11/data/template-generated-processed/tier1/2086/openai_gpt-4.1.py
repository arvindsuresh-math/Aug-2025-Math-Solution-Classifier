def solve():
    """Index: 2086.
    Returns: the total cost in dollars to fill all the jewelry displays.
    """
    # L1
    necklace_capacity = 12 # can hold 12 necklaces
    necklace_current = 5 # currently holds 5 necklaces
    necklaces_needed = necklace_capacity - necklace_current

    # L2
    necklace_price = 4 # $4 per necklace
    necklace_cost = necklaces_needed * necklace_price

    # L3
    ring_capacity = 30 # can hold 30 rings
    ring_current = 18 # currently holds 18 rings
    rings_needed = ring_capacity - ring_current

    # L4
    ring_price = 10 # $10 per ring
    ring_cost = rings_needed * ring_price

    # L5
    bracelet_capacity = 15 # can hold 15 bracelets
    bracelet_current = 8 # currently holds 8 bracelets
    bracelets_needed = bracelet_capacity - bracelet_current

    # L6
    bracelet_price = 5 # $5 per bracelet
    bracelet_cost = bracelets_needed * bracelet_price

    # L7
    total_cost = necklace_cost + ring_cost + bracelet_cost

    # FA
    answer = total_cost
    return answer