def solve():
    """Index: 3506.
    Returns: the total number of coins Rosie will get as change.
    """
    # L1
    bill_amount = 1 # $1 bill
    candy_cost = 0.44 # $.44 piece of candy
    change_amount = bill_amount - candy_cost

    # L3
    # The numbers of coins are stated in L2 of the solution and used in L3.
    num_quarters = 2 # 2 quarters
    num_nickels = 1 # 1 nickel
    num_pennies = 1 # 1 penny
    total_coins = num_quarters + num_nickels + num_pennies

    # FA
    answer = total_coins
    return answer