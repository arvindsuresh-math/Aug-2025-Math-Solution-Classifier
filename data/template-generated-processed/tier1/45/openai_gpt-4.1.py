def solve():
    """Index: 45.
    Returns: the total cost of the unicorn piñata and all the treats.
    """
    # L1
    reeses_bags = 4 # 4 bags of Reese's
    reeses_price_per_bag = 9 # $9 per bag
    reeses_total = reeses_price_per_bag * reeses_bags

    # L2
    snickers_bags = 3 # 3 bags of Snickers
    snickers_price_per_bag = 5 # $5 per bag
    snickers_total = snickers_price_per_bag * snickers_bags

    # L3
    skittles_bags = 5 # 5 bags of Skittles
    skittles_price_per_bag = 7 # $7 per bag
    skittles_total = skittles_price_per_bag * skittles_bags

    # L4
    pinata_price = 13 # unicorn piñata for $13
    total_cost = pinata_price + reeses_total + snickers_total + skittles_total

    # FA
    answer = total_cost
    return answer