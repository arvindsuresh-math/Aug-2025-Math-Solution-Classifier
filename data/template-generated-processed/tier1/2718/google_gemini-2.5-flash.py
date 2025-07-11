def solve():
    """Index: 2718.
    Returns: the total weight the marching band carries.
    """
    # L1
    num_trumpets = 6 # 6 trumpets
    num_clarinets = 9 # 9 clarinets
    total_trumpet_clarinet_players = num_trumpets + num_clarinets

    # L2
    weight_per_trumpet_clarinet = 5 # 5 pounds of weight
    total_weight_trumpet_clarinet = total_trumpet_clarinet_players * weight_per_trumpet_clarinet

    # L3
    num_trombones = 8 # 8 trombones
    weight_per_trombone = 10 # 10 pounds of weight
    total_weight_trombones = num_trombones * weight_per_trombone

    # L4
    num_tubas = 3 # 3 tubas
    weight_per_tuba = 20 # 20 pounds of weight
    total_weight_tubas = num_tubas * weight_per_tuba

    # L5
    num_drummers = 2 # 2 drummers
    weight_per_drummer = 15 # 15 pounds of weight
    total_weight_drummers = num_drummers * weight_per_drummer

    # L6
    total_band_weight = total_weight_trumpet_clarinet + total_weight_trombones + total_weight_tubas + total_weight_drummers

    # FA
    answer = total_band_weight
    return answer