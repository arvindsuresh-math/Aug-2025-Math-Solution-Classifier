def solve(
    paityn_red_hats: int = 20,  # Paityn has 20 red hats
    paityn_blue_hats: int = 24,  # Paityn has 24 blue hats
    zola_red_hats_ratio: float = 4/5,  # Zola has 4/5 times as many red hats
    zola_blue_hats_multiplier: int = 2  # Zola has twice the number of blue hats
):
    """Index: 83.
    Returns: the number of hats each person gets when they combine and share equally.
    """

    #: L1
    paityn_total_hats = paityn_red_hats + paityn_blue_hats # eval: 44 = 20 + 24

    #: L2
    zola_red_hats = zola_red_hats_ratio * paityn_red_hats # eval: 16.0 = 0.8 * 20

    #: L3
    zola_blue_hats = 49 # eval: 49 = 49

    #: L4
    zola_total_hats = zola_blue_hats + zola_red_hats # eval: 65.0 = 49 + 16.0

    #: L5
    total_combined_hats = zola_total_hats + paityn_total_hats # eval: 109.0 = 65.0 + 44

    #: L6
    hats_per_person = total_combined_hats / 2 # eval: 54.5 = 109.0 / 2

    #: FA
    answer = hats_per_person
    return answer # eval: return 54.5
