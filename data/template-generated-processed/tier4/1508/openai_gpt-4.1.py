def solve():
    """Index: 1508.
    Returns: the total amount Dorothy and Jemma made from selling glass frames.
    """
    # L1
    jemma_frames_sold = 400 # Jemma sold 400 frames
    jemma_price_per_frame = 5 # Jemma sells the glass frames at 5 dollars each
    jemma_total = jemma_frames_sold * jemma_price_per_frame

    # L2
    dorothy_frames_sold = jemma_frames_sold / 2 # Jemma sold twice as many frames as Dorothy

    # L3
    dorothy_price_per_frame = jemma_price_per_frame / 2 # Dorothy sells glass frames at half the price that Jemma sells them

    # L4
    dorothy_total = dorothy_price_per_frame * dorothy_frames_sold

    # L5
    total_made = jemma_total + dorothy_total

    # FA
    answer = total_made
    return answer