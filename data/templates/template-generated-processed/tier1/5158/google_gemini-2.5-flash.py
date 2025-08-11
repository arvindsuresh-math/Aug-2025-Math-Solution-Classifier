def solve():
    """Index: 5158.
    Returns: the total number of different movies seen by the club members.
    """
    # L1
    dalton_total_movies = 7 # Dalton watched 7 movies
    movies_watched_together = 2 # They all watched 2 movies together
    dalton_unique_movies = dalton_total_movies - movies_watched_together

    # L2
    hunter_total_movies = 12 # Hunter watched 12
    hunter_unique_movies = hunter_total_movies - movies_watched_together

    # L3
    alex_total_movies = 15 # Alex watched 15
    alex_unique_movies = alex_total_movies - movies_watched_together

    # L4
    total_different_movies = movies_watched_together + dalton_unique_movies + hunter_unique_movies + alex_unique_movies

    # FA
    answer = total_different_movies
    return answer