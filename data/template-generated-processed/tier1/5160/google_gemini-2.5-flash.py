def solve():
    """Index: 5160.
    Returns: the total number of more ducks and geese Rayden has than Lily.
    """
    # L1
    rayden_duck_multiplier = 3 # three times as many ducks as Lily
    lily_ducks = 20 # Lily bought 20 ducks
    rayden_ducks = rayden_duck_multiplier * lily_ducks

    # L2
    rayden_more_ducks = rayden_ducks - lily_ducks

    # L3
    rayden_geese_multiplier = 4 # four times as many geese as Lily
    lily_geese = 10 # Lily bought 10 geese
    rayden_geese = rayden_geese_multiplier * lily_geese

    # L4
    rayden_more_geese = rayden_geese - lily_geese

    # L5
    total_more_animals = rayden_more_geese + rayden_more_ducks

    # FA
    answer = total_more_animals
    return answer