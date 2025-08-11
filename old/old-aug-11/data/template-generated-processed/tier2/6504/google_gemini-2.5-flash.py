def solve():
    """Index: 6504.
    Returns: Bob's total profit from the side business.
    """
    # L1
    num_dogs = 2 # 2 show dogs
    cost_per_dog = 250.00 # $250.00 each
    total_dog_cost = num_dogs * cost_per_dog

    # L2
    num_puppies = 6 # litter of 6 puppies
    price_per_puppy = 350.00 # sells each puppy for $350.00
    total_puppy_revenue = num_puppies * price_per_puppy

    # L3
    total_profit = total_puppy_revenue - total_dog_cost

    # FA
    answer = total_profit
    return answer