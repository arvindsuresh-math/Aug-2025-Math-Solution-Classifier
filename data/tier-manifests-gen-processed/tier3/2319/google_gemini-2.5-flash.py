from fractions import Fraction

def solve():
    """Index: 2319.
    Returns: the total amount the friend should pay.
    """
    # L1
    cost_per_dog = 1000 # Corgi dogs for $1000 each
    profit_percentage = Fraction(30, 100) # 30% profit
    profit_per_dog = cost_per_dog * profit_percentage

    # L2
    selling_price_per_dog = cost_per_dog + profit_per_dog

    # L3
    number_of_dogs = 2 # two dogs
    total_cost_for_friend = selling_price_per_dog * number_of_dogs

    # FA
    answer = total_cost_for_friend
    return answer