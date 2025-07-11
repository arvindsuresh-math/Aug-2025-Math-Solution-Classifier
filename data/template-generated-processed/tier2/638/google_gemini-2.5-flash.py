def solve():
    """Index: 638.
    Returns: the profit James made from the lotto tickets.
    """
    # L1
    num_tickets = 200 # 200 lotto tickets
    cost_per_ticket = 2 # 2 dollars each
    total_spent = num_tickets * cost_per_ticket

    # L2
    winner_percent = 0.2 # 20% are winners
    num_winner_tickets = num_tickets * winner_percent

    # L3
    five_dollar_winner_percent = 0.8 # 80% of the winners are for 5 dollars
    num_five_dollar_winners = num_winner_tickets * five_dollar_winner_percent

    # L4
    five_dollar_prize = 5 # for 5 dollars
    total_five_dollar_winnings = num_five_dollar_winners * five_dollar_prize

    # L5
    num_other_winners = num_winner_tickets - num_five_dollar_winners

    # L6
    grand_prize_ticket_count = 1 # 1 ticket is the grand prize
    num_ten_dollar_winners = num_other_winners - grand_prize_ticket_count

    # L7
    average_other_prize = 10 # The other tickets win an average of $10
    total_ten_dollar_winnings = average_other_prize * num_ten_dollar_winners

    # L8
    grand_prize_amount = 5000 # $5,000
    profit = grand_prize_amount + total_ten_dollar_winnings + total_five_dollar_winnings - total_spent

    # FA
    answer = profit
    return answer