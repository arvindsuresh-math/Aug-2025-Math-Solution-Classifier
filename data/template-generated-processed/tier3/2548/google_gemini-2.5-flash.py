def solve():
    """Index: 2548.
    Returns: the total number of vessels on the water.
    """
    # L1
    cruise_ships = 4 # 4 cruise ships
    cargo_ship_multiplier = 2 # twice as many cargo ships
    cargo_ships = cruise_ships * cargo_ship_multiplier

    # L2
    more_sailboats = 6 # 6 more than the cargo ships
    sailboats = cargo_ships + more_sailboats

    # L3
    fishing_boat_multiplier = 7 # seven times more than fishing boats
    fishing_boats = sailboats / fishing_boat_multiplier

    # L4
    total_vessels = cruise_ships + cargo_ships + sailboats + fishing_boats

    # FA
    answer = total_vessels
    return answer