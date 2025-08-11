def solve():
    """Index: 6238.
    Returns: the amount each friend should contribute to the total expenses.
    """
    # L1
    ticket_price = 7 # $7 each
    num_friends = 3 # Three friends
    total_ticket_cost = ticket_price * num_friends

    # L2
    popcorn_price_per_box = 1.5 # $1.5
    num_popcorn_boxes = 2 # 2 boxes of popcorn
    total_popcorn_cost = popcorn_price_per_box * num_popcorn_boxes

    # L3
    milk_tea_price_per_cup = 3 # $3 each
    num_milk_tea_cups = 3 # 3 cups of milk tea
    total_milk_tea_cost = milk_tea_price_per_cup * num_milk_tea_cups

    # L4
    total_expenses = total_ticket_cost + total_popcorn_cost + total_milk_tea_cost

    # L5
    contribution_per_person = total_expenses / num_friends

    # FA
    answer = contribution_per_person
    return answer