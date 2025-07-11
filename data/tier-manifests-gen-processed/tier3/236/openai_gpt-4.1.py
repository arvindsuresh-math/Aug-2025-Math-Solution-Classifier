def solve():
    """Index: 236.
    Returns: the amount of money Jake has left after all transactions.
    """
    # L1
    initial_money = 5000 # Jake has $5000
    motorcycle_cost = 2800 # spends $2800 on a new motorcycle
    after_motorcycle = initial_money - motorcycle_cost

    # L2
    concert_divisor = 2 # spends half of what's left
    after_concert = after_motorcycle / concert_divisor

    # L3
    loss_divisor = 4 # loses a fourth of what he has left
    lost_amount = after_concert / loss_divisor

    # L4
    final_amount = after_concert - lost_amount

    # FA
    answer = final_amount
    return answer