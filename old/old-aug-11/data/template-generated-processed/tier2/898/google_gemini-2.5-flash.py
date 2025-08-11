def solve():
    """Index: 898.
    Returns: the final length of the rope after tying.
    """
    # L1
    rope_length_8ft = 8 # an 8-foot rope
    rope_length_20ft = 20 # a 20-foot rope
    rope_length_2ft = 2 # three 2 foot ropes
    num_2ft_ropes = 3 # three 2 foot ropes
    rope_length_7ft = 7 # a 7-foot rope
    combined_length = rope_length_8ft + rope_length_20ft + (rope_length_2ft * num_2ft_ropes) + rope_length_7ft

    # L2
    num_knots = 5 # derived from 1 (8ft) + 1 (20ft) + 3 (2ft) + 1 (7ft) = 6 pieces of rope, requiring 6-1=5 knots
    loss_per_knot = 1.2 # lose 1.2 foot per knot
    total_loss_from_knots = num_knots * loss_per_knot

    # L3
    final_length = combined_length - total_loss_from_knots

    # FA
    answer = final_length
    return answer