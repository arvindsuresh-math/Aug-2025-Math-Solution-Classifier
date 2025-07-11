def solve():
    """Index: 2407.
    Returns: the total number of pieces of bread and treats that Wanda and Jane brought.
    """
    # L1
    wanda_bread_pieces = 90 # Wanda brings 90 pieces of bread
    wanda_bread_treats_multiplier = 3 # three times as many pieces of bread as treats
    wanda_treats = wanda_bread_pieces / wanda_bread_treats_multiplier

    # L2
    jane_treats_multiplier = 2 # half as many treats as Jane (meaning Jane has twice as many)
    jane_treats = wanda_treats * jane_treats_multiplier

    # L3
    jane_bread_treats_percent = 0.75 # Jane brings 75% as many pieces of bread as treats
    jane_bread_pieces = jane_bread_treats_percent * jane_treats

    # L4
    total_items = wanda_treats + jane_treats + jane_bread_pieces + wanda_bread_pieces

    # FA
    answer = total_items
    return answer