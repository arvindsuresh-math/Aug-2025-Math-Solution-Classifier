def solve():
    """Index: 1789.
    Returns: the total number of cards traded between Padma and Robert.
    """
    # L1
    padma_traded_valuable = 2 # traded 2 or her valuable ones
    padma_traded_for_robert_cards = 15 # traded another 8 of his cards for 15 of Padma's cards
    padma_total_traded = padma_traded_valuable + padma_traded_for_robert_cards

    # L2
    robert_traded_for_padma_cards = 10 # traded 2 or her valuable ones for 10 of Robert's cards
    robert_traded_another = 8 # traded another 8 of his cards
    robert_total_traded = robert_traded_for_padma_cards + robert_traded_another

    # L3
    total_cards_traded = padma_total_traded + robert_total_traded

    # FA
    answer = total_cards_traded
    return answer