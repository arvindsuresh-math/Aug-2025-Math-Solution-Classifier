from fractions import Fraction

def solve():
    """Index: 7208.
    Returns: the total amount of money received from the sale of the puppies.
    """
    # L1
    puppies_per_dog = 10 # 10 puppies each
    total_puppies = puppies_per_dog + puppies_per_dog

    # L2
    fraction_sold = Fraction(3, 4) # 3/4 of the puppies
    puppies_sold = fraction_sold * total_puppies

    # L3
    price_per_puppy = 200 # each at $200
    total_money_received = puppies_sold * price_per_puppy

    # FA
    answer = total_money_received
    return answer