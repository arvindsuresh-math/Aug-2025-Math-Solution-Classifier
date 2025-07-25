def solve():
    """Index: 3677.
    Returns: the number of cans of pie filling the pumpkin patch will produce.
    """
    # L1
    total_money_earned = 96 # made $96 selling pumpkins
    cost_per_pumpkin = 3 # $3 per person for a pumpkin
    pumpkins_sold = total_money_earned / cost_per_pumpkin

    # L2
    total_pumpkins_grown = 83 # grew 83 pumpkins this year
    pumpkins_left = total_pumpkins_grown - pumpkins_sold

    # L3
    pumpkins_per_can = 3 # 3 pumpkins to a can
    cans_of_pie_filling = pumpkins_left / pumpkins_per_can

    # FA
    answer = cans_of_pie_filling
    return answer