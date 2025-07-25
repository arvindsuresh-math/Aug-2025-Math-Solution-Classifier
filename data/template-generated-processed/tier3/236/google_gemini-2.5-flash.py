def solve():
    """Index: 236.
    Returns: the amount of money Jake has left.
    """
    # L1
    initial_money = 5000 # Jake has $5000
    motorcycle_cost = 2800 # spends $2800 on a new motorcycle
    money_after_motorcycle = initial_money - motorcycle_cost

    # L2
    concert_ticket_divisor = 2 # spends half of what's left
    money_after_concert = money_after_motorcycle / concert_ticket_divisor

    # L3
    loss_divisor = 4 # loses a fourth of what he has left
    money_lost = money_after_concert / loss_divisor

    # L4
    money_left = money_after_concert - money_lost

    # FA
    answer = money_left
    return answer