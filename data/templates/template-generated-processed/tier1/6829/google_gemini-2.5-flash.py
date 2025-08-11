def solve():
    """Index: 6829.
    Returns: the total cost of Karen's fast-food order.
    """
    # L1
    burger_cost = 5 # 5-dollar burger
    sandwich_cost = 4 # 4-dollar sandwich
    food_cost = burger_cost + sandwich_cost

    # L2
    smoothie_cost_per_item = 4 # two 4-dollar smoothies
    smoothie_total_cost = smoothie_cost_per_item + smoothie_cost_per_item

    # L3
    total_order_cost = food_cost + smoothie_total_cost

    # FA
    answer = total_order_cost
    return answer