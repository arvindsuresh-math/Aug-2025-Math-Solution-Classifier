def solve():
    """Index: 277.
    Returns: the cost of each of the two other puppies.
    """
    # L1
    sale_price_per_puppy = 150 # $150 each
    num_puppies_on_sale = 3 # Three puppies are on sale
    cost_of_sale_puppies = sale_price_per_puppy * num_puppies_on_sale

    # L2
    total_cost_all_puppies = 800 # total cost of $800
    cost_of_other_puppies = total_cost_all_puppies - cost_of_sale_puppies

    # L3
    num_other_puppies = 2 # two other puppies
    cost_per_other_puppy = cost_of_other_puppies / num_other_puppies

    # FA
    answer = cost_per_other_puppy
    return answer