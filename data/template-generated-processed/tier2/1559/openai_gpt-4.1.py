def solve():
    """Index: 1559.
    Returns: the total amount Maci pays for the pens.
    """
    # L1
    num_blue_pens = 10 # ten blue pens
    blue_pen_cost = 0.10 # blue pen costs ten cents each
    blue_total = num_blue_pens * blue_pen_cost

    # L2
    red_pen_multiplier = 2 # red pen costs twice as much as the blue pen
    red_pen_cost = red_pen_multiplier * blue_pen_cost

    # L3
    num_red_pens = 15 # 15 red pens
    red_total = num_red_pens * red_pen_cost

    # L4
    # Note: The solution uses $3 and $1, which are the dollar values of red_total and blue_total, respectively.
    red_total_dollars = 3 # $3 for the red pens (from red_total)
    blue_total_dollars = 1 # $1 for the blue pens (from blue_total)
    total_cost = red_total_dollars + blue_total_dollars

    # FA
    answer = total_cost
    return answer