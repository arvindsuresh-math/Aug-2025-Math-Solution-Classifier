def solve():
    """Index: 2718.
    Returns: the total weight carried by the marching band.
    """
    # L1
    num_trumpets = 6 # 6 trumpets
    num_clarinets = 9 # 9 clarinets
    total_trumpet_clarinet_players = num_trumpets + num_clarinets

    # L2
    weight_per_trumpet_clarinet = 5 # each trumpet and clarinet player carries 5 pounds
    total_trumpet_clarinet_weight = total_trumpet_clarinet_players * weight_per_trumpet_clarinet

    # L3
    num_trombones = 8 # 8 trombones
    weight_per_trombone = 10 # each trombone player carries 10 pounds
    total_trombone_weight = num_trombones * weight_per_trombone

    # L4
    num_tubas = 3 # 3 tubas
    weight_per_tuba = 20 # each tuba player carries 20 pounds
    total_tuba_weight = num_tubas * weight_per_tuba

    # L5
    num_drummers = 2 # 2 drummers
    weight_per_drummer = 15 # each drum player carries 15 pounds
    total_drummer_weight = num_drummers * weight_per_drummer

    # L6
    total_weight = total_trumpet_clarinet_weight + total_trombone_weight + total_tuba_weight + total_drummer_weight

    # FA
    answer = total_weight
    return answer