def solve():
    """Index: 138.
    Returns: the total amount saved via discounts for 3 gallons of whole milk and 5 boxes of cereal.
    """
    # L1
    milk_normal_price = 3 # normally costs $3
    milk_discounted_price = 2 # now sold at $2
    milk_discount_per_gallon = milk_normal_price - milk_discounted_price

    # L2
    num_gallons = 3 # buy 3 gallons of whole milk
    milk_total_discount = milk_discount_per_gallon * num_gallons

    # L3
    cereal_discount_per_box = 1 # discount of $1
    num_boxes = 5 # 5 boxes of cereal
    cereal_total_discount = cereal_discount_per_box * num_boxes

    # L4
    total_savings = milk_total_discount + cereal_total_discount

    # FA
    answer = total_savings
    return answer