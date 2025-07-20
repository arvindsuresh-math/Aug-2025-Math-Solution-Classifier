def solve():
    """Index: 5687.
    Returns: the total amount Maddie spent on T-shirts.
    """
    # L1
    packs_white_tshirts = 2 # 2 packs of white T-shirts
    tshirts_per_pack_white = 5 # packs of 5
    num_white_tshirts = packs_white_tshirts * tshirts_per_pack_white

    # L2
    packs_blue_tshirts = 4 # 4 packs of blue T-shirts
    tshirts_per_pack_blue = 3 # packs of 3
    num_blue_tshirts = packs_blue_tshirts * tshirts_per_pack_blue

    # L3
    total_tshirts = num_white_tshirts + num_blue_tshirts

    # L4
    cost_per_tshirt = 3 # Each T-shirt cost $3
    total_spent = cost_per_tshirt * total_tshirts

    # FA
    answer = total_spent
    return answer