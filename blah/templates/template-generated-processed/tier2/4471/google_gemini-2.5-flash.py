def solve():
    """Index: 4471.
    Returns: how much more Alice needs to spend to get free delivery.
    """
    # L1
    chicken_pounds = 1.5 # 1.5 pounds of chicken
    chicken_price_per_pound = 6.00 # $6.00 per pound
    chicken_cost = chicken_pounds * chicken_price_per_pound

    # L2
    num_sweet_potatoes = 4 # 4 sweet potatoes
    sweet_potato_price_each = 0.75 # $0.75 each
    sweet_potatoes_cost = num_sweet_potatoes * sweet_potato_price_each

    # L3
    num_broccoli_heads = 2 # 2 heads of broccoli
    broccoli_price_each = 2.00 # $2.00 each
    broccoli_cost = num_broccoli_heads * broccoli_price_each

    # L4
    lettuce_cost = 3.00 # 1 pack of lettuce for $3.00
    cherry_tomatoes_cost = 2.50 # cherry tomatoes for $2.50
    brussel_sprouts_cost = 2.50 # a pound of Brussel sprouts for $2.50
    current_cart_total = chicken_cost + lettuce_cost + cherry_tomatoes_cost + sweet_potatoes_cost + broccoli_cost + brussel_sprouts_cost

    # L5
    free_delivery_minimum = 35.00 # minimum of $35.00
    additional_spend_needed = free_delivery_minimum - current_cart_total

    # FA
    answer = additional_spend_needed
    return answer