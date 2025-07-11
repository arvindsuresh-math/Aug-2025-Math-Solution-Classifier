def solve():
    """Index: 929.
    Returns: the total amount in dollars Tom spends on bricks.
    """
    # L1
    total_bricks = 1000 # Tom needs 1000 bricks
    half_divisor = 2 # half of the bricks
    half_bricks = total_bricks / half_divisor

    # L2
    full_price = 0.50 # $.50 per brick
    discount_divisor = 2 # 50% off
    half_price = full_price / discount_divisor

    # L3
    half_price_cost = half_bricks * half_price

    # L4
    full_price_cost = half_bricks * full_price

    # L5
    total_cost = half_price_cost + full_price_cost

    # FA
    answer = total_cost
    return answer