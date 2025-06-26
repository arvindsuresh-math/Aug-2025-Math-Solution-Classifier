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
    paityn_total_hats = paityn_red_hats + paityn_blue_hats

    #: L2
    zola_red_hats = zola_red_hats_ratio * paityn_red_hats

    #: L3
    zola_blue_hats = zola_blue_hats_multiplier * paityn_blue_hats

    #: L4
    zola_total_hats = zola_blue_hats + zola_red_hats

    #: L5
    total_combined_hats = zola_total_hats + paityn_total_hats

    #: L6
    hats_per_person = total_combined_hats / 2

    answer = hats_per_person  # FINAL ANSWER
    return answer