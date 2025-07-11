def solve():
    """Index: 638.
    Returns: the profit James made from buying the lotto tickets.
    """
    # L1
    num_tickets = 200 # James buys 200 lotto tickets
    ticket_price = 2 # for 2 dollars each
    total_spent = num_tickets * ticket_price

    # L2
    percent_winners = 0.2 # 20% are winners
    num_winning_tickets = num_tickets * percent_winners

    # L3
    percent_five_dollar = 0.8 # 80% of the winners are for 5 dollars
    num_five_dollar_winners = int(num_winning_tickets * percent_five_dollar)

    # L4
    five_dollar_prize = 5 # $5
    total_five_dollar_prize = num_five_dollar_winners * five_dollar_prize

    # L5
    num_other_winners = int(num_winning_tickets - num_five_dollar_winners)

    # L6
    num_grand_prize = 1 # 1 ticket is the grand prize
    num_ten_dollar_winners = num_other_winners - num_grand_prize

    # L7
    ten_dollar_prize = 10 # average of $10
    total_ten_dollar_prize = ten_dollar_prize * num_ten_dollar_winners

    # L8
    grand_prize = 5000 # $5,000
    total_winnings = grand_prize + total_ten_dollar_prize + total_five_dollar_prize
    profit = total_winnings - total_spent
    # FA
    answer = profit
    return answer