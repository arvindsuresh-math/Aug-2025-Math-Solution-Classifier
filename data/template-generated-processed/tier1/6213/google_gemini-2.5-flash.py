def solve():
    """Index: 6213.
    Returns: the amount of change Sally received.
    """
    # L1
    num_frames = 3 # 3 photograph frames
    cost_per_frame = 3 # each costing her $3
    total_cost_frames = num_frames * cost_per_frame

    # L2
    paid_amount = 20 # paid with a $20 bill
    change = paid_amount - total_cost_frames

    # FA
    answer = change
    return answer