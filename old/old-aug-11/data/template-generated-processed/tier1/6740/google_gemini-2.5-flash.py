def solve():
    """Index: 6740.
    Returns: the total amount of money Sally and Jolly have altogether.
    """
    # L1
    sally_would_have = 80 # If Sally had $20 less, she would have $80
    sally_less_amount = 20 # If Sally had $20 less
    sally_money = sally_would_have + sally_less_amount

    # L2
    jolly_would_have = 70 # If Jolly has $20 more, she would have $70
    jolly_more_amount = 20 # If Jolly has $20 more
    jolly_money = jolly_would_have - jolly_more_amount

    # L3
    total_money = sally_money + jolly_money

    # FA
    answer = total_money
    return answer