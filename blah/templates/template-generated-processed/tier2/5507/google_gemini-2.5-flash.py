def solve():
    """Index: 5507.
    Returns: the amount of weight John can put on the bar.
    """
    # L1
    max_support_weight = 1000 # support 1000 pounds
    safety_margin_percent = 0.2 # stay 20% under that weight
    safety_margin_amount = max_support_weight * safety_margin_percent

    # L2
    safe_max_weight = max_support_weight - safety_margin_amount

    # L3
    johns_weight = 250 # weighs 250 pounds
    weight_on_bar = safe_max_weight - johns_weight

    # FA
    answer = weight_on_bar
    return answer