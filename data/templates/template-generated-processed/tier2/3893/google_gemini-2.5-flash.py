def solve():
    """Index: 3893.
    Returns: the total amount of money Rocco has.
    """
    # L2
    coins_per_pile = 10 # piles of 10 coins each
    piles_of_quarters = 4 # 4 piles of quarters
    value_per_quarter = 0.25 # WK
    quarters_value = coins_per_pile * piles_of_quarters * value_per_quarter

    # L3
    piles_of_dimes = 6 # 6 piles of dimes
    value_per_dime = 0.10 # WK
    dimes_value = coins_per_pile * piles_of_dimes * value_per_dime

    # L4
    piles_of_nickels = 9 # 9 piles of nickels
    value_per_nickel = 0.05 # WK
    nickels_value = coins_per_pile * piles_of_nickels * value_per_nickel

    # L5
    piles_of_pennies = 5 # 5 piles of pennies
    value_per_penny = 0.01 # WK
    pennies_value = coins_per_pile * piles_of_pennies * value_per_penny

    # L6
    total_money = quarters_value + dimes_value + nickels_value + pennies_value

    # FA
    answer = total_money
    return answer