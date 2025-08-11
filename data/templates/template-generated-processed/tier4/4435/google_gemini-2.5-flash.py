def solve():
    """Index: 4435.
    Returns: the number of boxes of cookies Steve bought.
    """
    # L1
    num_cereal_boxes = 2 # two boxes of cereal
    cost_per_cereal_box = 3.5 # $3.5 each
    cost_cereal = num_cereal_boxes * cost_per_cereal_box

    # L2
    num_bananas = 4 # 4 bananas
    cost_per_banana = 0.25 # $.25 each
    cost_bananas = num_bananas * cost_per_banana

    # L3
    num_apples = 4 # four apples
    cost_per_apple = 0.5 # $.5 each
    cost_apples = num_apples * cost_per_apple

    # L4
    cost_milk = 3 # a gallon of milk for $3
    cost_other_items = cost_milk + cost_cereal + cost_bananas + cost_apples

    # L5
    total_groceries_cost = 25 # $25 worth of groceries
    cost_cookies = total_groceries_cost - cost_other_items

    # L6
    cost_milk_per_gallon = 3 # gallon of milk for $3
    cookie_cost_multiplier = 2 # twice as much per box as the gallon of milk
    cost_per_cookie_box = cost_milk_per_gallon * cookie_cost_multiplier

    # L7
    num_cookie_boxes = cost_cookies / cost_per_cookie_box

    # FA
    answer = num_cookie_boxes
    return answer