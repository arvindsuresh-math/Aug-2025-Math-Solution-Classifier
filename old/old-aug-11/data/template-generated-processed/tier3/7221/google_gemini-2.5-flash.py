def solve():
    """Index: 7221.
    Returns: the number of cases of muffins Nora must sell.
    """
    # L1
    muffin_price = 2 # prices each muffin at two dollars
    muffins_per_pack = 4 # Each pack has four muffins
    pack_price = 1 * muffin_price * muffins_per_pack

    # L2
    packs_per_case = 3 # Each case has three packs of muffins
    case_price = packs_per_case * pack_price

    # L3
    fundraising_goal = 120 # raise $120
    cases_needed = fundraising_goal / case_price

    # FA
    answer = cases_needed
    return answer