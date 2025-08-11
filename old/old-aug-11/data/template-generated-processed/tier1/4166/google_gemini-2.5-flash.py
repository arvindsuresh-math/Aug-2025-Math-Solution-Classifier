def solve():
    """Index: 4166.
    Returns: the total number of pennies Grace will have.
    """
    # L1
    num_dimes = 10 # 10 dimes
    pennies_per_dime = 10 # A dime has the same value as 10 pennies
    pennies_from_dimes = num_dimes * pennies_per_dime

    # L2
    num_nickels = 10 # 10 nickels
    pennies_per_nickel = 5 # a nickel has the same value as 5 pennies
    pennies_from_nickels = num_nickels * pennies_per_nickel

    # L3
    total_pennies = pennies_from_dimes + pennies_from_nickels

    # FA
    answer = total_pennies
    return answer