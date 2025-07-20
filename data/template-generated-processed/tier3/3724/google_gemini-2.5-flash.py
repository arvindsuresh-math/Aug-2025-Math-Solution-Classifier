def solve():
    """Index: 3724.
    Returns: the amount of money Bruce put in the bank.
    """
    # L1
    aunt_money = 75 # card with $75
    grandfather_money = 150 # card that had $150 in it
    total_birthday_money = aunt_money + grandfather_money

    # L2
    fraction_denominator = 5 # one-fifth of the money
    money_in_bank = total_birthday_money / fraction_denominator

    # FA
    answer = money_in_bank
    return answer