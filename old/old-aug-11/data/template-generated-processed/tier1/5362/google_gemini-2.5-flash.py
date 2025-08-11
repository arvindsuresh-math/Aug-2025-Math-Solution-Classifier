def solve():
    """Index: 5362.
    Returns: the total number of carriages in all towns.
    """
    # L1
    norwich_carriages = 100 # Norwich had 100 carriages
    flying_scotsman_more_than_norwich = 20 # 20 more carriages than Norwich
    flying_scotsman_carriages = norwich_carriages + flying_scotsman_more_than_norwich

    # L2
    flying_scotsman_norwich_total = flying_scotsman_carriages + norwich_carriages

    # L3
    euston_carriages = 130 # Euston had 130 carriages
    euston_more_than_norfolk = 20 # 20 more carriages than Norfolk
    norfolk_carriages = euston_carriages - euston_more_than_norfolk

    # L4
    euston_norfolk_total = norfolk_carriages + euston_carriages

    # L5
    total_carriages = euston_norfolk_total + flying_scotsman_norwich_total

    # FA
    answer = total_carriages
    return answer