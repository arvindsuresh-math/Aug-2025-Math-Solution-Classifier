def solve():
    """Index: 2755.
    Returns: the total amount of money Bowen spends.
    """
    # L1
    num_pens = 40 # Bowen buys 40 pens
    pencil_more_fraction_num = 2 # 2/5 times more pencils
    pencil_more_fraction_den = 5 # 2/5 times more pencils
    pencil_more_fraction = pencil_more_fraction_num / pencil_more_fraction_den
    more_pencils = pencil_more_fraction * num_pens

    # L2
    total_pencils = num_pens + more_pencils

    # L3
    pencil_price = 0.25 # each pencil costs twenty-five cents
    pencil_total_cost = total_pencils * pencil_price

    # L4
    pen_price = 0.15 # each pen sells at fifteen cents
    pen_total_cost = pen_price * num_pens

    # L5
    total_spent = pencil_total_cost + pen_total_cost

    # FA
    answer = total_spent
    return answer