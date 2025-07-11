def solve():
    """Index: 898.
    Returns: the final length of Tony's rope after tying all pieces together.
    """
    # L1
    rope1 = 8 # 8-foot rope
    rope2 = 20 # 20-foot rope
    rope3_length = 2 # 2 foot ropes
    rope3_count = 3 # three 2 foot ropes
    rope4 = 7 # 7-foot rope
    combined_length = rope1 + rope2 + (rope3_length * rope3_count) + rope4

    # L2
    num_knots = 5 # 5 knots (one less than number of ropes: 5 ropes)
    loss_per_knot = 1.2 # each knot ... lose 1.2 foot per knot
    total_knot_loss = num_knots * loss_per_knot

    # L3
    final_length = combined_length - total_knot_loss

    # FA
    answer = final_length
    return answer