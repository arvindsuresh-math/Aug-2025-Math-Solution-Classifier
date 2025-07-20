def solve():
    """Index: 5156.
    Returns: the total number of cows the man has now.
    """
    # L1
    initial_cows = 39 # 39 cows
    died_cows = 25 # 25 of them died
    sold_cows = 6 # sold 6 of them
    cows_after_last_year = initial_cows - died_cows - sold_cows

    # L2
    increased_cows = 24 # increased by 24
    cows_after_increase = cows_after_last_year + increased_cows

    # L3
    bought_cows = 43 # bought 43 more
    cows_after_bought = cows_after_increase + bought_cows

    # L4
    gift_cows = 8 # gave him 8 cows as a gift
    final_cows = cows_after_bought + gift_cows

    # FA
    answer = final_cows
    return answer