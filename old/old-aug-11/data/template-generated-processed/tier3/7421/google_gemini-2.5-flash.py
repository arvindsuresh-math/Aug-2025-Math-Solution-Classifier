def solve():
    """Index: 7421.
    Returns: the amount of dollars each of the next ten winners will receive.
    """
    # L1
    total_prize_money = 2400 # $2,400 in prize money
    first_winner_divisor = 3 # a third of the money
    first_winner_prize = total_prize_money / first_winner_divisor

    # L2
    remaining_money = total_prize_money - first_winner_prize

    # L3
    num_next_winners = 10 # The next ten winners
    prize_per_next_winner = remaining_money / num_next_winners

    # FA
    answer = prize_per_next_winner
    return answer