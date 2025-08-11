def solve():
    """Index: 7359.
    Returns: the cost of one pair of jeans.
    """
    # L1
    total_cost = 110 # The total cost of the items was $110
    coat_cost = 40 # a coat for $40
    shoes_cost = 30 # a pair of shoes for $30
    cost_of_two_jeans = total_cost - coat_cost - shoes_cost

    # L2
    number_of_jeans_pairs = 2 # two pairs of jeans
    cost_of_one_pair_of_jeans = cost_of_two_jeans / number_of_jeans_pairs

    # FA
    answer = cost_of_one_pair_of_jeans
    return answer