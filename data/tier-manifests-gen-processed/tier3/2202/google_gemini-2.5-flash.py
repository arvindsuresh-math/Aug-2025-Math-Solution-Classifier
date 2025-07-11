def solve():
    """Index: 2202.
    Returns: the total cost to use the boards for one day in dollars.
    """
    # L1
    ink_needed_per_whiteboard_ml = 20 # each whiteboard needs about 20ml of ink
    cost_per_ml_cents = 50 # ink costs 50 cents per ml
    cost_per_whiteboard_cents = ink_needed_per_whiteboard_ml * cost_per_ml_cents

    # L2
    whiteboards_per_class = 2 # Each class uses 2 whiteboards each
    cost_per_class_cents = whiteboards_per_class * cost_per_whiteboard_cents

    # L3
    num_classes = 5 # there are 5 classes
    total_cost_cents = num_classes * 1 * cost_per_class_cents

    # L4
    cents_per_dollar = 100 # 100 cents make a dollar
    total_cost_dollars = total_cost_cents / cents_per_dollar

    # FA
    answer = total_cost_dollars
    return answer