def solve():
    """Index: 5489.
    Returns: the number of models Kirsty can buy now.
    """
    # L1
    original_price_per_model = 0.45 # each one cost $0.45
    num_models_saved_for = 30 # buy 30 models
    total_money_saved = original_price_per_model * num_models_saved_for

    # L2
    new_price_per_model = 0.50 # price had increased to $0.50
    num_models_can_buy = total_money_saved / new_price_per_model

    # FA
    answer = num_models_can_buy
    return answer