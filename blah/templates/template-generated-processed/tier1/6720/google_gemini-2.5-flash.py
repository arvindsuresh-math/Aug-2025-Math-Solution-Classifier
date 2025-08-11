def solve():
    """Index: 6720.
    Returns: the total number of action figures Janet has.
    """
    # L1
    initial_figures = 10 # 10 action figures
    sells_figures = 6 # sells 6 of them
    figures_after_selling = initial_figures - sells_figures

    # L2
    buys_figures = 4 # get 4 that are in better condition
    figures_after_buying = figures_after_selling + buys_figures

    # L3
    brother_multiplier = 2 # twice the size
    brother_collection = brother_multiplier * figures_after_buying

    # L4
    total_figures = figures_after_buying + brother_collection

    # FA
    answer = total_figures
    return answer