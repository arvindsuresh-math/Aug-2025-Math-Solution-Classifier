def solve():
    """Index: 182.
    Returns: the total amount Lisa and Carly spent in dollars.
    """
    # L1
    lisa_tshirt_cost = 40 # Lisa spends $40 on t-shirts
    half_amount_divisor = 2 # half of this amount
    lisa_jeans_cost = lisa_tshirt_cost / half_amount_divisor

    # L2
    twice_amount_multiplier = 2 # twice this amount
    lisa_coats_cost = lisa_tshirt_cost * twice_amount_multiplier

    # L3
    lisa_total_spent = lisa_tshirt_cost + lisa_jeans_cost + lisa_coats_cost

    # L4
    carly_tshirt_divisor = 4 # only a quarter as much as Lisa on t-shirts
    carly_tshirt_cost = lisa_tshirt_cost / carly_tshirt_divisor

    # L5
    carly_jeans_multiplier = 3 # 3 times as much on jeans
    carly_jeans_cost = lisa_jeans_cost * carly_jeans_multiplier

    # L6
    carly_coats_divisor = 4 # a quarter of the amount Lisa spent on coats
    carly_coats_cost = lisa_coats_cost / carly_coats_divisor

    # L7
    carly_total_spent = carly_tshirt_cost + carly_jeans_cost + carly_coats_cost

    # L8
    total_spent = lisa_total_spent + carly_total_spent

    # FA
    answer = total_spent
    return answer