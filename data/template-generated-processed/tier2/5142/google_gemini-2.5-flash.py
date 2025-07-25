def solve():
    """Index: 5142.
    Returns: the money saved by buying a gallon of paint instead of 8 pints.
    """
    # L1
    num_pints_needed = 8 # 8 doors to paint / 8 separate pints of paint
    cost_per_pint = 8.00 # $8.00 a pint
    cost_8_separate_pints = num_pints_needed * cost_per_pint

    # L2
    cost_gallon_paint = 55.00 # a gallon of paint (which is the same as 8 pints) for a flat $55.00
    money_saved = cost_8_separate_pints - cost_gallon_paint

    # FA
    answer = money_saved
    return answer