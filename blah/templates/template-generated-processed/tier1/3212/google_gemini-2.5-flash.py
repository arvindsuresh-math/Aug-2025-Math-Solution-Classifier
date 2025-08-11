def solve():
    """Index: 3212.
    Returns: the total number of units in the condo.
    """
    # L1
    total_floors = 23 # 23 floors
    penthouse_floors = 2 # top 2 floors are assigned for penthouse units
    regular_floors = total_floors - penthouse_floors

    # L2
    units_per_regular_floor = 12 # Regular floors have 12 units
    total_regular_units = units_per_regular_floor * regular_floors

    # L3
    units_per_penthouse_floor = 2 # penthouse floors have only 2 units
    total_penthouse_units = units_per_penthouse_floor * penthouse_floors

    # L4
    total_units = total_regular_units + total_penthouse_units

    # FA
    answer = total_units
    return answer