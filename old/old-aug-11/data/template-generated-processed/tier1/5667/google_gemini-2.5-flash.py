def solve():
    """Index: 5667.
    Returns: the total amount spent by Leonard and Michael.
    """
    # L1
    num_sneakers_pairs = 2 # two pairs of sneakers
    cost_per_sneaker_pair = 100 # $100 each pair
    cost_sneakers = num_sneakers_pairs * cost_per_sneaker_pair

    # L2
    cost_wallet = 50 # a wallet at $50
    leonard_total_spent = cost_wallet + cost_sneakers

    # L3
    num_jeans_pairs = 2 # two pairs of jeans
    cost_per_jean_pair = 50 # $50 each pair
    cost_jeans = num_jeans_pairs * cost_per_jean_pair

    # L4
    cost_backpack = 100 # a backpack at $100
    michael_total_spent = cost_backpack + cost_jeans

    # L5
    total_spent_all = leonard_total_spent + michael_total_spent

    # FA
    answer = total_spent_all
    return answer