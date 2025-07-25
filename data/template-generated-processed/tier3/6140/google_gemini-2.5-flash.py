from fractions import Fraction

def solve():
    """Index: 6140.
    Returns: the total number of hours of their favorite movies together.
    """
    # L1
    nikki_movie_length = 30 # Nikki's favorite movie is 30 hours long
    ryn_fraction = Fraction(4, 5) # Ryn's favorite movie is 4/5 times as long
    ryn_movie_length = ryn_fraction * nikki_movie_length

    # L2
    nikki_ryn_total_length = ryn_movie_length + nikki_movie_length

    # L3
    michael_multiplier = 3 # three times as long as Michael's movie
    michael_movie_length = nikki_movie_length / michael_multiplier

    # L4
    nikki_ryn_michael_total_length = nikki_ryn_total_length + michael_movie_length

    # L5
    joyce_additional_hours = 2 # 2 hours longer than Michael's movie
    joyce_movie_length = michael_movie_length + joyce_additional_hours

    # L6
    total_all_movies_length = nikki_ryn_michael_total_length + joyce_movie_length

    # FA
    answer = total_all_movies_length
    return answer