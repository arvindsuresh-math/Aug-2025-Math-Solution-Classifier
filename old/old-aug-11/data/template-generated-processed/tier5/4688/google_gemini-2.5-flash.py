def solve():
    """Index: 4688.
    Returns: the cost of the shirt.
    """
    # L5
    total_cost = 600 # shirt and a coat for $600
    # The shirt is one-third the price of the coat, meaning the coat is 3 times the shirt's price.
    # So, total cost = shirt_price + coat_price = shirt_price + 3 * shirt_price = 4 * shirt_price.
    coefficient_for_shirt_price = 4 # derived from the relationship: 1 part shirt + 3 parts coat = 4 total parts
    shirt_price = total_cost / coefficient_for_shirt_price

    # FA
    answer = shirt_price
    return answer