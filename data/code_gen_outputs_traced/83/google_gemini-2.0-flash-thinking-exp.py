def solve(
    paityn_red_hats: int = 20, # Paityn has 20 red hats
    paityn_blue_hats: int = 24, # and 24 blue hats
    zola_red_hat_factor: float = 4/5, # Her friend Zola has 4/5 times as many red hats as she has
    zola_blue_hat_factor: int = 2, # and twice the number of blue hats
    num_people_sharing: int = 2 # share them equally between themselves
):
    """Index: 83.
    Returns: the number of hats each person gets after combining and sharing equally.
    """
    #: L1
    paityn_total_hats = paityn_red_hats + paityn_blue_hats # eval: 44 = 20 + 24
    #: L2
    zola_red_hats = zola_red_hat_factor * paityn_red_hats # eval: 16.0 = 0.8 * 20
    #: L3
    zola_blue_hats = zola_blue_hat_factor * paityn_blue_hats # eval: 48 = 2 * 24
    #: L4
    zola_total_hats = zola_blue_hats + zola_red_hats # eval: 64.0 = 48 + 16.0
    #: L5
    combined_hats = zola_total_hats + paityn_total_hats # eval: 108.0 = 64.0 + 44
    #: L6
    hats_per_person = combined_hats / num_people_sharing # eval: 54.0 = 108.0 / 2
    answer = hats_per_person # FINAL ANSWER # eval: 54.0 = 54.0 # FINAL ANSWER
    return answer # eval: return 54.0