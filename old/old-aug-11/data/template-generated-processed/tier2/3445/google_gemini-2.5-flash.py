def solve():
    """Index: 3445.
    Returns: the total money Mr. Parker saves.
    """
    # L1
    burger_price_individual = 5 # burger for $5
    fries_price_individual = 3 # french fries for $3
    soft_drink_price_individual = 3 # soft drink for $3
    individual_regular_cost = burger_price_individual + fries_price_individual + soft_drink_price_individual

    # L2
    kids_burger_price_individual = 3 # kid’s burger is $3
    kids_fries_price_individual = 2 # kid’s french fries are $2
    kids_juice_box_price_individual = 2 # kid's juice box is $2
    individual_kids_cost = kids_burger_price_individual + kids_fries_price_individual + kids_juice_box_price_individual

    # L3
    special_burger_meal_price = 9.50 # special burger meal, you get all 3 of these food items for $9.50
    savings_per_regular_meal = individual_regular_cost - special_burger_meal_price

    # L4
    kids_meal_price = 5 # kids meal of all 3 kids' food items for $5
    savings_per_kids_meal = individual_kids_cost - kids_meal_price

    # L5
    num_adult_burger_meals_mr_parker = 2 # 2 burger meals for his wife and himself
    num_adult_burger_meals_children = 2 # 2 burger meals and 2 kid's meals for his 4 children
    num_total_burger_meals = num_adult_burger_meals_mr_parker + num_adult_burger_meals_children
    total_savings_regular_meals = num_total_burger_meals * savings_per_regular_meal

    # L6
    num_kids_meals_children = 2 # 2 kid's meals for his 4 children
    total_savings_kids_meals = num_kids_meals_children * savings_per_kids_meal

    # L7
    total_savings = total_savings_regular_meals + total_savings_kids_meals

    # FA
    answer = total_savings
    return answer