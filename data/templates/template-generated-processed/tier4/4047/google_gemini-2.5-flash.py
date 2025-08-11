def solve():
    """Index: 4047.
    Returns: the total amount Marcia will spend on her wardrobe.
    """
    # L1
    pants_price = 30.00 # both pairs of pants are $30.00 each
    discount_fraction = 0.5 # 1/2 off
    second_pair_pants_cost = pants_price * discount_fraction

    # L2
    total_pants_cost = pants_price + second_pair_pants_cost

    # L3
    skirt_price = 20.00 # skirts are $20.00 each
    num_skirts = 3 # add 3 skirts
    total_skirts_cost = skirt_price * num_skirts

    # L4
    blouse_price = 15.00 # blouses are $15.00
    num_blouses = 5 # add 5 blouses
    total_blouses_cost = blouse_price * num_blouses

    # L5
    total_wardrobe_cost = total_pants_cost + total_skirts_cost + total_blouses_cost

    # FA
    answer = total_wardrobe_cost
    return answer