def solve():
    """Index: 736.
    Returns: the total cost of Hilary's meal including tip, in dollars.
    """
    # L1
    num_samosas = 3 # three samosas
    samosa_price = 2 # $2 each
    samosas_cost = num_samosas * samosa_price

    # L2
    num_pakoras = 4 # four orders of pakoras
    pakora_price = 3 # $3 each
    pakoras_cost = num_pakoras * pakora_price

    # L3
    mango_lassi_price = 2 # a mango lassi, for $2
    food_total = samosas_cost + pakoras_cost + mango_lassi_price

    # L4
    tip_percent = 0.25 # 25% tip
    tip_amount = food_total * tip_percent

    # L5
    total_cost = food_total + tip_amount

    # FA
    answer = total_cost
    return answer