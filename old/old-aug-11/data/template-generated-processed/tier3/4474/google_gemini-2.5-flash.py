def solve():
    """Index: 4474.
    Returns: the amount of money Alison has.
    """
    # L1
    kent_money = 1000 # Kent has $1,000
    brooke_multiplier = 2 # Brooke has twice as much money as Kent
    brooke_money = brooke_multiplier * kent_money

    # L2
    brittany_multiplier = 4 # Brittany has 4 times as much money as Brooke
    brittany_money = brittany_multiplier * brooke_money

    # L3
    alison_divisor = 2 # Alison has half as much money as Brittany
    alison_money = brittany_money / alison_divisor

    # FA
    answer = alison_money
    return answer