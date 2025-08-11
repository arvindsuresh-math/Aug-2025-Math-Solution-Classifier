def solve():
    """Index: 5001.
    Returns: the total money Gretchen made.
    """
    # L1
    drawings_saturday = 24 # 24 on Saturday
    drawings_sunday = 16 # 16 on Sunday
    total_drawings = drawings_saturday + drawings_sunday

    # L2
    charge_per_drawing = 20.00 # $20.00 per drawing
    total_money_made = charge_per_drawing * total_drawings

    # FA
    answer = total_money_made
    return answer