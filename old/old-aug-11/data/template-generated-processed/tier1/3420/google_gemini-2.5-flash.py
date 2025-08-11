def solve():
    """Index: 3420.
    Returns: the total earnings if Jimmy sells all the figures.
    """
    # L1
    num_figures_common_value = 4 # Four of the five figures
    common_figure_value = 15 # worth $15
    value_common_figures = num_figures_common_value * common_figure_value

    # L2
    expensive_figure_value = 20 # one which is worth $20
    total_original_value = value_common_figures + expensive_figure_value

    # L3
    num_total_figures = 5 # collection of 5 action figures
    discount_per_figure = 5 # sell each of them for $5 less
    total_discount = num_total_figures * discount_per_figure

    # L4
    total_earnings = total_original_value - total_discount

    # FA
    answer = total_earnings
    return answer