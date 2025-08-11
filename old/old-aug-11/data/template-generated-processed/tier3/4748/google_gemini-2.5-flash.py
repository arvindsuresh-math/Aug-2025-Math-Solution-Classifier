def solve():
    """Index: 4748.
    Returns: the initial amount of money in the cookie jar.
    """
    # L1
    doris_spent = 6 # Doris spent $6 from the cookie jar
    half_divisor = 2 # half as much as Doris
    martha_spent = doris_spent / half_divisor

    # L2
    total_spent = doris_spent + martha_spent

    # L3
    money_left = 15 # $15 left in the cookie jar
    initial_money = money_left + total_spent

    # FA
    answer = initial_money
    return answer