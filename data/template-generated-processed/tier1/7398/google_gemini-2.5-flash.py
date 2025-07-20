def solve():
    """Index: 7398.
    Returns: the number of walnuts left in the burrow.
    """
    # L1
    walnuts_already_there = 12 # 12 already there
    boy_gathers = 6 # gathers 6 walnuts
    walnuts_after_boy_gathers = walnuts_already_there + boy_gathers

    # L2
    boy_drops = 1 # dropping 1 on the way
    walnuts_after_boy_drops = walnuts_after_boy_gathers - boy_drops

    # L3
    girl_brings = 5 # brings 5 more walnuts
    walnuts_after_girl_brings = walnuts_after_boy_drops + girl_brings

    # L4
    girl_eats = 2 # eats 2
    final_walnuts = walnuts_after_girl_brings - girl_eats

    # FA
    answer = final_walnuts
    return answer