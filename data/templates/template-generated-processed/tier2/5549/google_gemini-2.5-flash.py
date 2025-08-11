def solve():
    """Index: 5549.
    Returns: the total amount Jasmine will pay.
    """
    # L1
    coffee_pounds = 4 # 4 pounds of coffee beans
    coffee_price_per_pound = 2.50 # $2.50
    cost_of_coffee = coffee_pounds * coffee_price_per_pound

    # L2
    milk_gallons = 2 # 2 gallons of milk
    milk_price_per_gallon = 3.50 # $3.50
    cost_of_milk = milk_price_per_gallon * milk_gallons

    # L3
    total_cost = cost_of_coffee + cost_of_milk

    # FA
    answer = total_cost
    return answer