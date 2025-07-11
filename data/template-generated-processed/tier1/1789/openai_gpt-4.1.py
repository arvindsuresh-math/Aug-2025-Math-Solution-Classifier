def solve():
    """Index: 1789.
    Returns: the total number of cards traded between Padma and Robert.
    """
    # L1
    padma_first_trade = 2 # traded 2 of her valuable ones
    padma_second_trade = 15 # traded 15 of Padma's cards
    padma_total_traded = padma_first_trade + padma_second_trade

    # L2
    robert_first_trade = 10 # traded 10 of Robert's cards
    robert_second_trade = 8 # traded another 8 of his cards
    robert_total_traded = robert_first_trade + robert_second_trade

    # L3
    total_traded = padma_total_traded + robert_total_traded

    # FA
    answer = total_traded
    return answer