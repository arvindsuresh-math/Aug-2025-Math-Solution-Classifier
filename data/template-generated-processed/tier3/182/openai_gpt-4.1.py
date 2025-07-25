def solve():
    """Index: 182.
    Returns: the total amount Lisa and Carly spent in dollars.
    """
    # L1
    lisa_tshirt = 40 # Lisa spends $40 on t-shirts
    lisa_jeans_divisor = 2 # spends half of this amount on jeans
    lisa_jeans = lisa_tshirt / lisa_jeans_divisor

    # L2
    lisa_coats_multiplier = 2 # twice this amount on coats
    lisa_coats = lisa_tshirt * lisa_coats_multiplier

    # L3
    lisa_total = lisa_tshirt + lisa_jeans + lisa_coats

    # L4
    carly_tshirt_divisor = 4 # Carly spends only a quarter as much as Lisa on t-shirts
    carly_tshirt = lisa_tshirt / carly_tshirt_divisor

    # L5
    carly_jeans_multiplier = 3 # spends 3 times as much on jeans
    carly_jeans = lisa_jeans * carly_jeans_multiplier

    # L6
    carly_coats_divisor = 4 # a quarter of the amount Lisa spent on coats
    carly_coats = lisa_coats / carly_coats_divisor

    # L7
    carly_total = carly_tshirt + carly_jeans + carly_coats

    # L8
    answer = lisa_total + carly_total
    return answer