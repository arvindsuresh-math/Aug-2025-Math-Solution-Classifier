def solve():
    """Index: 1697.
    Returns: the amount of money left in the cookie jar.
    """
    # L1
    doris_spent = 6 # Doris spent $6 from the cookie jar
    half_divisor = 2 # half as much as Doris
    martha_spent = doris_spent / half_divisor

    # L2
    total_spent = doris_spent + martha_spent

    # L3
    initial_money = 21 # There were 21 dollars in the cookie jar
    money_left = initial_money - total_spent

    # FA
    answer = money_left
    return answer