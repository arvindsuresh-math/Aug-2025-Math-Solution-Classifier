def solve():
    """Index: 2164.
    Returns: the number of dolls in the box.
    """
    # L1
    total_toys = 24 # 24 toys in the box
    fraction_action_figures = 1/4 # 1/4 of them are action figures
    action_figures = fraction_action_figures * total_toys

    # L2
    dolls = total_toys - action_figures

    # FA
    answer = dolls
    return answer