def solve():
    """Index: 283.
    Returns: the amount of money the lottery winner will receive as the prize.
    """
    # L1
    first_ticket_price = 1 # sells the first ticket for $1
    increment = 1 # each successive ticket for a dollar more
    second_ticket_price = first_ticket_price + increment

    # L2
    third_ticket_price = second_ticket_price + increment

    # L3
    fourth_ticket_price = third_ticket_price + increment

    # L4
    fifth_ticket_price = fourth_ticket_price + increment

    # L5
    total_collected = first_ticket_price + second_ticket_price + third_ticket_price + fourth_ticket_price + fifth_ticket_price

    # L6
    profit = 4 # keep a $4 profit
    prize_money = total_collected - profit

    # FA
    answer = prize_money
    return answer