def solve():
    """Index: 4561.
    Returns: the total money all three have in dollars.
    """
    # L1
    jack_money = 26 # Jack has $26
    ben_less_than_jack = 9 # Ben has $9 less than Jack
    ben_money = jack_money - ben_less_than_jack

    # L2
    eric_less_than_ben = 10 # Eric has $10 less than Ben
    eric_money = ben_money - eric_less_than_ben

    # L3
    total_money = jack_money + ben_money + eric_money

    # FA
    answer = total_money
    return answer