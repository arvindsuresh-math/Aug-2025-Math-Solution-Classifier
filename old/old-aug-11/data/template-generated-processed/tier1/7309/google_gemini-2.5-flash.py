def solve():
    """Index: 7309.
    Returns: the total number of balls of wool used by Enid and Aaron.
    """
    # L1
    aaron_scarves = 10 # Aaron makes 10 scarves
    wool_per_scarf = 3 # a scarf uses 3 balls of wool
    aaron_wool_for_scarves = aaron_scarves * wool_per_scarf

    # L2
    aaron_sweaters = 5 # and 5 sweaters
    wool_per_sweater = 4 # a sweater uses 4 balls of wool
    aaron_wool_for_sweaters = aaron_sweaters * wool_per_sweater

    # L3
    enid_sweaters = 8 # Enid makes 8 sweaters
    enid_wool_for_sweaters = enid_sweaters * wool_per_sweater

    # L4
    total_wool = aaron_wool_for_scarves + aaron_wool_for_sweaters + enid_wool_for_sweaters

    # FA
    answer = total_wool
    return answer