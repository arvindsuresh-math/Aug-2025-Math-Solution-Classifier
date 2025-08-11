def solve():
    """Index: 138.
    Returns: the total savings via discounts for buying milk and cereal.
    """
    # L1
    original_milk_cost = 3 # normally costs $3
    discounted_milk_cost = 2 # now sold at $2
    milk_discount_per_gallon = original_milk_cost - discounted_milk_cost

    # L2
    num_gallons_milk = 3 # buy 3 gallons of whole milk
    total_milk_discount = milk_discount_per_gallon * num_gallons_milk

    # L3
    cereal_discount_per_box = 1 # discount of $1
    num_boxes_cereal = 5 # 5 boxes of cereal
    total_cereal_discount = cereal_discount_per_box * num_boxes_cereal

    # L4
    total_savings = total_milk_discount + total_cereal_discount

    # FA
    answer = total_savings
    return answer