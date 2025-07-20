def solve():
    """Index: 5544.
    Returns: the total sale amount from the potatoes.
    """
    # L1
    initial_potatoes_kg = 6500 # 6500 kg of potatoes
    damaged_potatoes_kg = 150 # 150 kg are damaged
    sellable_potatoes_kg = initial_potatoes_kg - damaged_potatoes_kg

    # L2
    bag_capacity_kg = 50 # 50 kg bags
    num_bags = sellable_potatoes_kg / bag_capacity_kg

    # L3
    price_per_bag = 72 # each bag being sold for $72
    total_sale_amount = num_bags * price_per_bag

    # FA
    answer = total_sale_amount
    return answer