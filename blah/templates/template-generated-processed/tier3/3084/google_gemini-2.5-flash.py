def solve():
    """Index: 3084.
    Returns: the total number of berries Susan will pick.
    """
    # L1
    total_berries_per_handful = 5 # every handful of 5 strawberries
    eaten_berries_per_handful = 1 # eat one of them herself
    berries_in_basket_per_handful = total_berries_per_handful - eaten_berries_per_handful

    # L2
    basket_capacity = 60 # basket holds 60 strawberries
    handfuls_to_fill_basket = basket_capacity / berries_in_basket_per_handful

    # L3
    total_berries_picked = basket_capacity + handfuls_to_fill_basket * eaten_berries_per_handful

    # FA
    answer = total_berries_picked
    return answer