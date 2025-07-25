def solve():
    """Index: 814.
    Returns: the total amount Sean spent.
    """
    # L1
    num_flavored_croissants = 2 # 1 almond croissant and 1 salami and cheese croissant
    flavored_croissant_price = 4.50 # $4.50 each
    flavored_croissants_total = num_flavored_croissants * flavored_croissant_price

    # L2
    num_lattes = 2 # 2 lattes
    latte_price = 2.50 # $2.50 each
    lattes_total = num_lattes * latte_price

    # L3
    plain_croissant_price = 3.00 # plain croissant for $3.00
    focaccia_price = 4.00 # loaf of focaccia for $4.00
    total_spent = flavored_croissants_total + lattes_total + plain_croissant_price + focaccia_price

    # FA
    answer = total_spent
    return answer