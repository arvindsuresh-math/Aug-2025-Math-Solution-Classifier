def solve():
    """Index: 5676.
    Returns: the total number of tiles Don, Ken, Laura, and Kim can paint in 15 minutes.
    """
    # L1
    don_paint_rate = 3 # Don can paint 3 tiles a minute
    ken_more_than_don = 2 # Ken can paint 2 more tiles a minute than Don
    ken_paint_rate = don_paint_rate + ken_more_than_don

    # L2
    laura_multiplier_ken = 2 # Laura can paint twice as many tiles as Ken
    laura_paint_rate = ken_paint_rate * laura_multiplier_ken

    # L3
    kim_fewer_than_laura = 3 # Kim can paint 3 fewer tiles than Laura
    kim_paint_rate = laura_paint_rate - kim_fewer_than_laura

    # L4
    total_paint_rate_per_minute = don_paint_rate + ken_paint_rate + laura_paint_rate + kim_paint_rate

    # L5
    total_minutes = 15 # in 15 minutes
    total_tiles_painted = total_minutes * total_paint_rate_per_minute

    # FA
    answer = total_tiles_painted
    return answer