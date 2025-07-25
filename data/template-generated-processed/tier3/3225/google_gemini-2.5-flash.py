def solve():
    """Index: 3225.
    Returns: the average price paid per movie.
    """
    # L1
    dvd_quantity = 8 # 8 movies on DVD
    dvd_price = 12 # $12 each
    bluray_quantity = 4 # 4 movies on Blu-ray
    bluray_price = 18 # $18 each
    total_spent = dvd_quantity * dvd_price + bluray_quantity * bluray_price

    # L2
    total_movies = dvd_quantity + bluray_quantity

    # L3
    average_price = total_spent / total_movies

    # FA
    answer = average_price
    return answer