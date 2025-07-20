def solve():
    """Index: 4844.
    Returns: the total number of pieces of candy Brent had left.
    """
    # L1
    kit_kat_bars = 5 # 5 Kit-Kat bars
    kisses_multiplier = 3 # three times that amount in Hershey kisses
    hershey_kisses = kit_kat_bars * kisses_multiplier

    # L2
    baby_ruths = 10 # 10 Baby Ruths
    reese_divisor = 2 # half that amount in Reese Peanut butter cups
    reese_cups = baby_ruths / reese_divisor

    # L3
    initial_lollipops = 11 # 11 lollipops
    lollipops_given_away = 5 # giving his little sister 5 lollipops
    remaining_lollipops = initial_lollipops - lollipops_given_away

    # L4
    nerds_boxes = 8 # 8 boxes of Nerds
    total_candy = kit_kat_bars + hershey_kisses + baby_ruths + reese_cups + nerds_boxes + remaining_lollipops

    # FA
    answer = total_candy
    return answer