def solve():
    """Index: 3004.
    Returns: the money saved by using raspberries instead of blueberries.
    """
    # L1
    ounces_per_batch = 12 # each batch takes 12 ounces of fruit
    num_batches = 4 # make 4 batches of muffins
    total_ounces_needed = ounces_per_batch * num_batches

    # L2
    blueberry_ounces_per_carton = 6 # Blueberries cost $5.00 per 6 ounce carton
    num_blueberry_cartons = total_ounces_needed / blueberry_ounces_per_carton

    # L3
    cost_per_blueberry_carton = 5 # Blueberries cost $5.00 per 6 ounce carton
    total_blueberry_cost = num_blueberry_cartons * cost_per_blueberry_carton

    # L4
    raspberry_ounces_per_carton = 8 # raspberries cost $3.00 per 8 ounce carton
    num_raspberry_cartons = total_ounces_needed / raspberry_ounces_per_carton

    # L5
    cost_per_raspberry_carton = 3 # raspberries cost $3.00 per 8 ounce carton
    total_raspberry_cost = num_raspberry_cartons * cost_per_raspberry_carton

    # L6
    money_saved = total_blueberry_cost - total_raspberry_cost

    # FA
    answer = money_saved
    return answer