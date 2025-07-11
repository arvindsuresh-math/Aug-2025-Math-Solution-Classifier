def solve():
    """Index: 2382.
    Returns: the total amount of money Christy and Tanya spent together.
    """
    # L1
    price_per_face_moisturizer = 50 # pays 50$ for two face moisturizers each
    num_face_moisturizers = 2 # two face moisturizers
    tanya_face_total = price_per_face_moisturizer * num_face_moisturizers

    # L2
    num_body_lotions = 4 # buying four of them
    price_per_body_lotion = 60 # 60$ per body lotion
    tanya_body_total = num_body_lotions * price_per_body_lotion

    # L3
    tanya_total = tanya_body_total + tanya_face_total

    # L4
    christy_multiplier = 2 # Christy spends twice as much as Tanya
    christy_total = christy_multiplier * tanya_total

    # L5
    total_spent = christy_total + tanya_total

    # FA
    answer = total_spent
    return answer