def solve(
    ratio_elsa: int = 10, # The ratio of coins that Elsa has to that which Amalie has is 10:45
    ratio_amalie: int = 45, # The ratio of coins that Elsa has to that which Amalie has is 10:45
    total_coins: int = 440, # the total number of coins they have is 440
    amalie_fraction_spent: float = 3/4 # Amalie spends 3/4 of what she has on toys
):
    """Index: 68.
    Returns: the number of coins Amalie will remain with after spending some of them.
    """
    #: L1
    total_ratio = ratio_elsa + ratio_amalie # eval: 55 = 10 + 45
    #: L2
    amalie_coins = (ratio_amalie / total_ratio) * total_coins # eval: 360.0 = (45 / 55) * 440
    #: L3
    amalie_spent_coins = amalie_fraction_spent * amalie_coins # eval: 270.0 = 0.75 * 360.0
    #: L4
    amalie_remaining_coins = amalie_coins - amalie_spent_coins # eval: 90.0 = 360.0 - 270.0
    answer = amalie_remaining_coins # FINAL ANSWER # eval: 90.0 = 90.0 # FINAL ANSWER
    return answer # eval: return 90.0