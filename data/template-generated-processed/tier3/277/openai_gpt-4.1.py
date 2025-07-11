def solve():
    """Index: 277.
    Returns: the cost of each of the two other puppies.
    """
    # L1
    sale_price_per_puppy = 150 # $150 each (three puppies are on sale for $150 each)
    sale_puppies = 3 # Three puppies on sale
    sale_total = sale_price_per_puppy * sale_puppies

    # L2
    total_cost = 800 # total cost of $800
    other_puppies_cost = total_cost - sale_total

    # L3
    other_puppies = 2 # two other puppies
    each_other_puppy_cost = other_puppies_cost / other_puppies

    # FA
    answer = each_other_puppy_cost
    return answer