def solve():
    """Index: 3023.
    Returns: the number of packs of stickers Dora received.
    """
    # L1
    allowance_per_person = 9 # allowance of $9 each
    number_of_people = 2 # Lola and Dora combined their allowance
    combined_allowance = allowance_per_person * number_of_people

    # L2
    cost_of_cards = 10 # deck of playing cards for $10
    money_after_cards = combined_allowance - cost_of_cards

    # L3
    cost_per_pack_stickers = 2 # $2 boxes of stickers
    num_sticker_packs = money_after_cards / cost_per_pack_stickers

    # L4
    people_splitting_stickers = 2 # split the boxes evenly
    dora_sticker_packs = num_sticker_packs / people_splitting_stickers

    # FA
    answer = dora_sticker_packs
    return answer