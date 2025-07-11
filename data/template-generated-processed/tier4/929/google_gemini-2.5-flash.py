def solve():
    """Index: 929.
    Returns: the total dollars Tom spends on bricks.
    """
    # L1
    total_bricks = 1000 # 1000 bricks
    half_divisor = 2 # half of the bricks
    bricks_half_price = total_bricks / half_divisor

    # L2
    full_price_per_brick = 0.50 # $.50
    discount_divisor = 2 # 50% off
    price_per_brick_half_price = full_price_per_brick / discount_divisor

    # L3
    cost_half_price_bricks = bricks_half_price * price_per_brick_half_price

    # L4
    cost_full_price_bricks = bricks_half_price * full_price_per_brick

    # L5
    total_cost = cost_half_price_bricks + cost_full_price_bricks

    # FA
    answer = total_cost
    return answer