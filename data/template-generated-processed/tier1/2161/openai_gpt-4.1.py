def solve():
    """Index: 2161.
    Returns: the amount of money Renata ended up having.
    """
    # L1
    initial_money = 10 # Renata had $10 to spend
    charity_ticket = 4 # made a $4 donation in exchange for a ticket
    after_charity = initial_money - charity_ticket

    # L2
    prize_money = 90 # winner of the 5th prize of $90
    after_prize = after_charity + prize_money

    # L3
    casino_loss1 = 50 # lost $50 at the first slot machine
    casino_loss2 = 10 # $10 at the second
    casino_loss3 = 5 # $5 at the last one
    total_casino_loss = casino_loss1 + casino_loss2 + casino_loss3

    # L4
    after_casino = after_prize - total_casino_loss

    # L5
    water_cost = 1 # $1 bottle of water
    lottery_ticket_cost = 1 # $1 lottery ticket
    total_gas_station_spend = water_cost + lottery_ticket_cost

    # L6
    after_gas_station = after_casino - total_gas_station_spend

    # L7
    lottery_win = 65 # won an instant prize of $65
    final_money = after_gas_station + lottery_win

    # FA
    answer = final_money
    return answer