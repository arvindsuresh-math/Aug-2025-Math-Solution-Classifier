from fractions import Fraction

def solve():
    """Index: 7125.
    Returns: the number of bottles Pete needs to return to the store.
    """
    # L1
    num_20_bills = 2 # two $20 bills
    value_20_bill = 20 # $20 bills
    wallet_money = num_20_bills * value_20_bill

    # L2
    num_10_bills = 4 # four $10 bills
    value_10_bill = 10 # $10 bills
    pocket_money = num_10_bills * value_10_bill

    # L3
    total_money_on_hand = wallet_money + pocket_money

    # L4
    bike_debt = 90 # last $90 he owes on a bike
    money_needed = bike_debt - total_money_on_hand

    # L5
    cents_per_bottle = 50 # 50 cents for each bottle
    bottle_value_fraction = Fraction(1, 2) # WK
    reciprocal_factor = 2 # WK
    bottles_needed = money_needed / bottle_value_fraction

    # FA
    answer = bottles_needed
    return answer