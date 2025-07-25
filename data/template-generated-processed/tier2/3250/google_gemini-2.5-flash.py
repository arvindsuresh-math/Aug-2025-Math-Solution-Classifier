def solve():
    """Index: 3250.
    Returns: how much James paid for the stickers.
    """
    # L1
    num_packs = 4 # 4 packs of stickers
    stickers_per_pack = 30 # 30 stickers each
    total_stickers = num_packs * stickers_per_pack

    # L2
    cost_per_sticker = 0.1 # $.10
    total_cost = total_stickers * cost_per_sticker

    # L3
    friend_pays_fraction = 0.5 # half
    james_payment = total_cost * friend_pays_fraction

    # FA
    answer = james_payment
    return answer