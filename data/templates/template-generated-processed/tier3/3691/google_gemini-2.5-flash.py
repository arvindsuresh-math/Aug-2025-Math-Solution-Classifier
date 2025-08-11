def solve():
    """Index: 3691.
    Returns: the total money Nathan makes from his harvest.
    """
    # L1
    strawberry_plants = 5 # 5 strawberry plants
    strawberries_per_plant = 14 # 14 strawberries from each plant
    total_strawberries = strawberry_plants * strawberries_per_plant

    # L2
    tomato_plants = 7 # 7 tomato plants
    tomatoes_per_plant = 16 # 16 tomatoes from each plant
    total_tomatoes = tomato_plants * tomatoes_per_plant

    # L3
    basket_capacity = 7 # baskets of 7
    strawberry_baskets = total_strawberries / basket_capacity

    # L4
    tomato_baskets = total_tomatoes / basket_capacity

    # L5
    strawberry_basket_price = 9 # sold a basket of strawberries for $9
    money_from_strawberries = strawberry_baskets * strawberry_basket_price

    # L6
    tomato_basket_price = 6 # a basket of tomatoes for $6
    money_from_tomatoes = tomato_baskets * tomato_basket_price

    # L7
    total_money = money_from_strawberries + money_from_tomatoes

    # FA
    answer = total_money
    return answer