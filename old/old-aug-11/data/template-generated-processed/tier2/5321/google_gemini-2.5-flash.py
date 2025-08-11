def solve():
    """Index: 5321.
    Returns: the total amount Julia will spend on the new puppy.
    """
    # L1
    treat_cost_per_bag = 2.50 # 2 bags of treats for $2.50 a bag
    num_treat_bags = 2 # 2 bags of treats
    treats_total_cost = treat_cost_per_bag * num_treat_bags

    # L2
    crate_bed_cost_each = 20.00 # a crate and a bed for $20.00 each
    num_crate_bed_items = 2 # WK
    crate_bed_total_cost = num_crate_bed_items * crate_bed_cost_each

    # L3
    dog_food_cost = 20.00 # a bag of dog food for $20.00
    toys_cost = 15.00 # an assortment box of toys for $15.00
    collar_leash_cost = 15.00 # the collar/leash combo for $15.00
    total_supplies_before_discount = dog_food_cost + treats_total_cost + toys_cost + crate_bed_total_cost + collar_leash_cost

    # L4
    discount_percent_decimal = 0.20 # from solution text: .20*95
    discount_percent_num = 20 # 20% new-customer discount
    percent_factor = 0.01 # WK
    discount_amount = discount_percent_decimal * total_supplies_before_discount

    # L5
    supplies_cost_after_discount = total_supplies_before_discount - discount_amount

    # L6
    puppy_adoption_cost = 20.00 # puppy for $20.00
    grand_total_cost = supplies_cost_after_discount + puppy_adoption_cost

    # FA
    answer = grand_total_cost
    return answer