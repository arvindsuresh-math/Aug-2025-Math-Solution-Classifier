def solve():
    """Index: 1983.
    Returns: the percentage of her grocery budget spent on meat, rounded to the nearest percent.
    """
    # L1
    broccoli_pounds = 3 # 3 pounds of broccoli
    broccoli_price_per_pound = 4 # $4 a pound
    total_broccoli_cost = broccoli_pounds * broccoli_price_per_pound

    # L2
    num_oranges = 3 # 3 oranges
    orange_price_each = 0.75 # $0.75 each
    total_orange_cost = num_oranges * orange_price_each

    # L3
    cabbage_cost = 3.75 # a cabbage for $3.75
    total_vegetable_cost = total_broccoli_cost + total_orange_cost + cabbage_cost

    # L4
    chicken_price_per_pound = 3 # $3 a pound
    chicken_pounds = 2 # two pounds of chicken
    total_chicken_cost = chicken_price_per_pound * chicken_pounds

    # L5
    bacon_cost = 3 # a pound of bacon for $3
    total_meat_cost = total_chicken_cost + bacon_cost

    # L6
    total_grocery_cost = total_meat_cost + total_vegetable_cost

    # L7
    percentage_factor = 100 # WK
    meat_percentage = round((total_meat_cost / total_grocery_cost) * percentage_factor)

    # FA
    answer = meat_percentage
    return answer