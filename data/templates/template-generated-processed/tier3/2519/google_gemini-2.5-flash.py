def solve():
    """Index: 2519.
    Returns: the price charged per action figure.
    """
    # L1
    sneaker_cost = 90 # sneakers which cost $90
    money_left_after_buying = 25 # still has $25 left after buying the sneakers
    money_before_buying = sneaker_cost + money_left_after_buying

    # L2
    money_already_saved = 15 # He already has $15 saved
    money_earned_from_figures = money_before_buying - money_already_saved

    # L3
    num_action_figures = 10 # If he sells 10 action figures
    price_per_action_figure = money_earned_from_figures / num_action_figures

    # FA
    answer = price_per_action_figure
    return answer