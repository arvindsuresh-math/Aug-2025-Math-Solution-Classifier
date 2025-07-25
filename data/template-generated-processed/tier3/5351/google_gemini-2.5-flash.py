def solve():
    """Index: 5351.
    Returns: the total number of golf carts Ellen needs.
    """
    # L1
    patrons_from_cars = 12 # 12 patrons who came in cars
    patrons_from_bus = 27 # 27 from a bus
    total_patrons_needing_ride = patrons_from_cars + patrons_from_bus

    # L2
    patrons_per_cart = 3 # Ellen can fit 3 patrons in a golf cart
    total_carts_needed = total_patrons_needing_ride / patrons_per_cart

    # FA
    answer = total_carts_needed
    return answer