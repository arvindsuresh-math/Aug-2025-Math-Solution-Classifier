def solve():
    """Index: 814.
    Returns: the total amount Sean spent.
    """
    # L1
    num_flavored_croissants = 2 # 1 almond croissant and 1 salami and cheese croissant
    cost_per_flavored_croissant = 4.50 # $4.50 each
    cost_flavored_croissants = num_flavored_croissants * cost_per_flavored_croissant

    # L2
    num_lattes = 2 # 2 lattes
    cost_per_latte = 2.50 # $2.50 each
    cost_lattes = num_lattes * cost_per_latte

    # L3
    cost_plain_croissant = 3.00 # a plain croissant for $3.00
    cost_focaccia = 4.00 # a loaf of focaccia for $4.00
    total_spent = cost_flavored_croissants + cost_lattes + cost_plain_croissant + cost_focaccia

    # FA
    answer = total_spent
    return answer