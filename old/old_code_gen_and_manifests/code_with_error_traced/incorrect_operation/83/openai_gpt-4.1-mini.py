def solve(
    paityn_red_hats: int = 20,  # Paityn has 20 red hats
    paityn_blue_hats: int = 24,  # Paityn has 24 blue hats
    zola_red_fraction: float = 4/5,  # Zola has 4/5 times as many red hats as Paityn
    zola_blue_multiplier: int = 2  # Zola has twice the number of blue hats as Paityn
):
    """Index: 83.
    Returns: the number of hats each person gets after combining and sharing equally.
    """

    #: L1
    paityn_total_hats = paityn_red_hats + paityn_blue_hats # eval: 44 = 20 + 24

    #: L2
    zola_red_hats = zola_red_fraction + paityn_red_hats # eval: 20.8 = 0.8 + 20

    #: L3
    zola_blue_hats = zola_blue_multiplier * paityn_blue_hats # eval: 48 = 2 * 24

    #: L4
    zola_total_hats = zola_red_hats + zola_blue_hats # eval: 68.8 = 20.8 + 48

    #: L5
    combined_hats = zola_total_hats + paityn_total_hats # eval: 112.8 = 68.8 + 44

    #: L6
    hats_per_person = combined_hats / 2 # eval: 56.4 = 112.8 / 2

    #: FA
    answer = hats_per_person
    return answer # eval: return 56.4
