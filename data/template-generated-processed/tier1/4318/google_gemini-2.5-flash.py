def solve():
    """Index: 4318.
    Returns: the total money Mell and her friends needed to pay at the cafeteria.
    """
    # L1
    num_friends_bought_ice_cream = 2 # Two of her friends ordered the same, but each of them also bought a bowl of ice cream
    cost_ice_cream = 3 # a bowl of ice cream is $3
    cost_friends_ice_cream = num_friends_bought_ice_cream * cost_ice_cream

    # L2
    cups_coffee_per_person = 2 # two cups of coffee
    num_people_total = 3 # Mell + two friends = 3 people
    total_cups_coffee = cups_coffee_per_person * num_people_total

    # L3
    cost_coffee_per_cup = 4 # One cup of coffee is $4
    total_cost_coffee = total_cups_coffee * cost_coffee_per_cup

    # L4
    num_friends_bought_cake = 3 # Mell ordered one piece of cake. Two of her friends ordered the same, so 3 people bought cake.
    cost_cake_per_piece = 7 # one piece of cake is $7
    total_cost_cake = num_friends_bought_cake * cost_cake_per_piece

    # L5
    total_money_paid = cost_friends_ice_cream + total_cost_coffee + total_cost_cake

    # FA
    answer = total_money_paid
    return answer