def solve():
    """Index: 4055.
    Returns: the number of candies the candy seller had left.
    """
    # L1
    candies_per_person = 20 # sold 20 candies, to each of the clowns and the children
    num_clowns = 4 # four clowns
    candies_sold_to_clowns = candies_per_person * num_clowns

    # L2
    num_children = 30 # thirty children
    candies_sold_to_children = candies_per_person * num_children

    # L3
    total_candies_sold = candies_sold_to_children + candies_sold_to_clowns

    # L4
    initial_candies = 700 # had 700 candies
    candies_left = initial_candies - total_candies_sold

    # FA
    answer = candies_left
    return answer