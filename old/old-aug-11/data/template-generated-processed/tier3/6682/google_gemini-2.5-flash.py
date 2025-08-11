def solve():
    """Index: 6682.
    Returns: the number of coins Beth sold.
    """
    # L1
    initial_coins_in_solution = 135 # Value from solution line L1's calculation
    gift_coins_in_solution = 25 # Value from solution line L1's calculation
    total_coins_after_gift = initial_coins_in_solution + gift_coins_in_solution

    # L2
    sell_divisor = 2 # sell half of her coins
    coins_sold = total_coins_after_gift / sell_divisor

    # FA
    answer = coins_sold
    return answer