def solve():
    """Index: 1508.
    Returns: the total amount made by Dorothy and Jemma from the sale of glass frames.
    """
    # L1
    jemma_frames_sold = 400 # Jemma sold 400 frames
    jemma_price_per_frame = 5 # 5 dollars each
    jemma_total_made = jemma_frames_sold * jemma_price_per_frame

    # L2
    jemma_frames_multiplier = 2 # twice as many frames as Dorothy
    dorothy_frames_sold = jemma_frames_sold / jemma_frames_multiplier

    # L3
    dorothy_price_divisor = 2 # half the price
    dorothy_price_per_frame = jemma_price_per_frame / dorothy_price_divisor

    # L4
    dorothy_total_made = dorothy_price_per_frame * dorothy_frames_sold

    # L5
    total_made_together = jemma_total_made + dorothy_total_made

    # FA
    answer = total_made_together
    return answer