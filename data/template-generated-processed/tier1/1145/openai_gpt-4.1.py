def solve():
    """Index: 1145.
    Returns: the amount of money Daria needs to earn to buy tickets for herself and three friends.
    """
    # L1
    num_people = 4 # tickets for her and for three of her friends
    ticket_cost = 90 # One ticket cost is $90
    total_cost = num_people * ticket_cost

    # L2
    current_money = 189 # Daria currently has $189
    money_needed = total_cost - current_money

    # FA
    answer = money_needed
    return answer