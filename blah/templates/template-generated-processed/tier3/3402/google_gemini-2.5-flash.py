def solve():
    """Index: 3402.
    Returns: the amount of money saved by the deal.
    """
    # L1
    movie_ticket_cost = 8 # Normally, a movie ticket costs $8
    popcorn_cost_reduction = 3 # a bucket of popcorn costs three dollars less
    popcorn_cost = movie_ticket_cost - popcorn_cost_reduction

    # L2
    drink_cost_increase = 1 # a drink costs a dollar more than popcorn
    drink_cost = popcorn_cost + drink_cost_increase

    # L3
    candy_cost_divisor = 2 # a candy costs half as much as a drink
    candy_cost = drink_cost / candy_cost_divisor

    # L4
    normal_price = movie_ticket_cost + popcorn_cost + drink_cost + candy_cost

    # L5
    deal_price = 20 # for $20
    savings = normal_price - deal_price

    # FA
    answer = savings
    return answer