def solve():
    """Index: 2487.
    Returns: the total amount the baker has to pay for all ingredients.
    """
    # L1
    flour_boxes = 3 # 3 boxes of flour
    flour_price_per_box = 3 # $3 each box
    flour_total = flour_boxes * flour_price_per_box

    # L2
    egg_trays = 3 # 3 trays of eggs
    egg_price_per_tray = 10 # $10 for each tray
    eggs_total = egg_trays * egg_price_per_tray

    # L3
    milk_liters = 7 # 7 liters of milk
    milk_price_per_liter = 5 # $5 each liter
    milk_total = milk_liters * milk_price_per_liter

    # L4
    baking_soda_boxes = 2 # 2 boxes of baking soda
    baking_soda_price_per_box = 3 # $3 each box
    baking_soda_total = baking_soda_boxes * baking_soda_price_per_box

    # L5
    total_cost = flour_total + eggs_total + milk_total + baking_soda_total

    # FA
    answer = total_cost
    return answer