def solve():
    """Index: 283.
    Returns: the amount of money the winner of the lottery will receive.
    """
    # L1
    first_ticket_price = 1 # sells the first ticket for $1
    price_increase_per_ticket = 1 # sells each successive ticket for a dollar more
    second_ticket_price = first_ticket_price + price_increase_per_ticket

    # L2
    third_ticket_price = second_ticket_price + price_increase_per_ticket

    # L3
    fourth_ticket_price = third_ticket_price + price_increase_per_ticket

    # L4
    fifth_ticket_price = fourth_ticket_price + price_increase_per_ticket

    # L5
    total_money_collected = first_ticket_price + second_ticket_price + third_ticket_price + fourth_ticket_price + fifth_ticket_price

    # L6
    profit_kept = 4 # keep a $4 profit
    prize_money = total_money_collected - profit_kept

    # FA
    answer = prize_money
    return answer