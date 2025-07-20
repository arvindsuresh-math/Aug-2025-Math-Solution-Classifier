def solve():
    """Index: 7426.
    Returns: the selling price of one bag of apples.
    """
    # L1
    apples_given_to_restaurant = 60 # 60 kg were given to a restaurant
    apples_for_juice = 90 # 90 kg were used to make fruit juice
    apples_used_or_given = apples_given_to_restaurant + apples_for_juice

    # L2
    total_harvested_apples = 405 # We harvested 405 kg of apples
    apples_sold = total_harvested_apples - apples_used_or_given

    # L3
    bag_weight = 5 # sold in 5 kg bags
    number_of_bags_sold = apples_sold / bag_weight

    # L4
    total_sale_revenue = 408 # their sale brought in $408
    price_per_bag = total_sale_revenue / number_of_bags_sold

    # FA
    answer = price_per_bag
    return answer