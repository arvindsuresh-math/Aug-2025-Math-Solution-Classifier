def solve():
    """Index: 4647.
    Returns: the total money Monica took to the bank.
    """
    # L1
    money_per_week = 15 # put $15 into her moneybox
    weeks_to_fill = 60 # took 60 weeks
    money_per_fill = money_per_week * weeks_to_fill

    # L2
    num_repetitions = 5 # repeated this whole process 5 times
    total_money = num_repetitions * money_per_fill

    # FA
    answer = total_money
    return answer