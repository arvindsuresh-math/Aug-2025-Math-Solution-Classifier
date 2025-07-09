def solve(
    total_spent: int = 75,  # For $75 she bought items
    num_shorts: int = 5,  # 5 pairs of shorts
    price_per_short: int = 7,  # $7 each
    num_shoes: int = 2,  # 2 pairs of shoes
    price_per_shoe: int = 10,  # $10 each
    num_tops: int = 4  # 4 tops
):
    """Index: 23.
    Returns: the cost of each top."""

    #: L1
    total_shorts_cost = num_shorts * price_per_short

    #: L2
    total_shoes_cost = num_shoes * price_per_shoe

    #: L3
    total_shorts_and_shoes_cost = total_shorts_cost * total_shoes_cost

    #: L4
    remaining_money = total_spent - total_shorts_and_shoes_cost

    #: L5
    cost_per_top = remaining_money / num_tops

    #: FA
    answer = cost_per_top
    return answer