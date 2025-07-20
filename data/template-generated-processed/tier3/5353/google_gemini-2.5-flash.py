def solve():
    """Index: 5353.
    Returns: the number of kittens the pet shop has.
    """
    # L1
    num_puppies = 2 # 2 puppies
    cost_per_puppy = 20 # A puppy costs $20
    cost_of_puppies = num_puppies * cost_per_puppy

    # L2
    total_stock_value = 100 # If the stock is worth $100
    cost_of_kittens = total_stock_value - cost_of_puppies

    # L3
    cost_per_kitten = 15 # a kitten costs $15
    num_kittens = cost_of_kittens / cost_per_kitten

    # FA
    answer = num_kittens
    return answer