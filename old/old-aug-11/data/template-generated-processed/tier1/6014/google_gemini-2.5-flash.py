def solve():
    """Index: 6014.
    Returns: the total cost of everything.
    """
    # L1
    num_soda_cans = 3 # 3 cans of soda
    cost_per_soda = 1 # soda cost $1
    total_soda_cost = num_soda_cans * cost_per_soda

    # L2
    num_soups = 2 # 2 soups
    cost_per_soup = total_soda_cost # Each soup cost as much as the 3 combined sodas
    total_soup_cost = num_soups * cost_per_soup

    # L3
    sandwich_cost_multiplier = 3 # The sandwich cost 3 times as much as the soup
    total_sandwich_cost = sandwich_cost_multiplier * cost_per_soup

    # L4
    total_cost = total_soda_cost + total_soup_cost + total_sandwich_cost

    # FA
    answer = total_cost
    return answer