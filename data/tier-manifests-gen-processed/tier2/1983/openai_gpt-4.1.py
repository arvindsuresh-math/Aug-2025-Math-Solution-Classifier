def solve():
    """Index: 1983.
    Returns: the percentage of Janet's grocery budget spent on meat, rounded to the nearest percent.
    """
    # L1
    broccoli_pounds = 3 # 3 pounds of broccoli
    broccoli_price_per_pound = 4 # $4 a pound
    broccoli_total = broccoli_pounds * broccoli_price_per_pound

    # L2
    orange_count = 3 # 3 oranges
    orange_price_each = 0.75 # $0.75 each
    orange_total = orange_count * orange_price_each

    # L3
    cabbage_price = 3.75 # a cabbage for $3.75
    vegetable_total = broccoli_total + orange_total + cabbage_price

    # L4
    chicken_price_per_pound = 3 # $3 a pound
    chicken_pounds = 2 # two pounds of chicken
    chicken_total = chicken_price_per_pound * chicken_pounds

    # L5
    bacon_price = 3 # a pound of bacon for $3
    meat_total = chicken_total + bacon_price

    # L6
    grocery_total = meat_total + vegetable_total

    # L7
    percent_factor = 100 # WK
    meat_percent = meat_total / grocery_total * percent_factor
    meat_percent_rounded = round(meat_percent)

    # FA
    answer = meat_percent_rounded
    return answer