from fractions import Fraction

def solve():
    """Index: 4845.
    Returns: the total amount Mike spent on shopping that day.
    """
    # L1
    food_cost = 30 # Mike spent $30
    wallet_more_than_food = 60 # The wallet is $60 more than the cost of the food
    wallet_cost = food_cost + wallet_more_than_food

    # L2
    shirt_fraction = Fraction(1, 3) # The shirt costs a third of the value of the wallet
    shirt_cost = shirt_fraction * wallet_cost

    # L3
    total_spent = food_cost + shirt_cost + wallet_cost

    # FA
    answer = total_spent
    return answer