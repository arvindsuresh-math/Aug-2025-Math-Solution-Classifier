def solve():
    """Index: 2161.
    Returns: the amount of money Renata ended up having.
    """
    # L1
    initial_money = 10 # Renata had $10 to spend
    donation_cost = 4 # made a $4 donation
    money_after_donation = initial_money - donation_cost

    # L2
    prize_money = 90 # winner of the 5th prize of $90
    money_after_prize = money_after_donation + prize_money

    # L3
    loss_slot_1 = 50 # lost $50 at the first slot machine
    loss_slot_2 = 10 # lost $10 at the second
    loss_slot_3 = 5 # lost $5 at the last one
    total_casino_loss = loss_slot_1 + loss_slot_2 + loss_slot_3

    # L4
    money_after_casino = money_after_prize - total_casino_loss

    # L5
    water_cost = 1 # picked a $1 bottle of water
    lottery_ticket_cost = 1 # bought a $1 lottery ticket
    total_walk_spend = water_cost + lottery_ticket_cost

    # L6
    money_after_walk_spend = money_after_casino - total_walk_spend

    # L7
    instant_prize = 65 # won an instant prize of $65
    final_money = money_after_walk_spend + instant_prize

    # FA
    answer = final_money
    return answer