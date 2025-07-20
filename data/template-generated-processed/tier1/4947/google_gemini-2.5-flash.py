def solve():
    """Index: 4947.
    Returns: the total money Tony has won.
    """
    # L1
    num_lottery_tickets = 3 # 3 lottery tickets
    winning_numbers_per_ticket = 5 # 5 of the numbers on each lottery ticket are winning numbers
    total_winning_numbers = num_lottery_tickets * winning_numbers_per_ticket

    # L2
    value_per_winning_number = 20 # each winning number is worth $20
    total_money_won = total_winning_numbers * value_per_winning_number

    # FA
    answer = total_money_won
    return answer