def solve():
    """Index: 4423.
    Returns: the number of servings of soda each guest gets.
    """
    # L1
    monica_money = 15 # Monica brings $15
    michelle_money = 12 # Michelle brings $12
    total_money = monica_money + michelle_money

    # L2
    cake_cost = 15 # The cake costs 15 dollars
    money_for_soda = total_money - cake_cost

    # L3
    soda_bottle_cost = 3 # soda is $3 a bottle
    num_soda_bottles = money_for_soda / soda_bottle_cost

    # L4
    servings_per_bottle = 12 # Each bottle of soda has 12 servings
    total_servings_soda = num_soda_bottles * servings_per_bottle

    # L5
    total_guests = 8 # If there are 8 total guests
    servings_per_guest = total_servings_soda / total_guests

    # FA
    answer = servings_per_guest
    return answer