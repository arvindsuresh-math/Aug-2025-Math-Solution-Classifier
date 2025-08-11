from fractions import Fraction

def solve():
    """Index: 961.
    Returns: the total number of movies produced by both companies in five years.
    """
    # L1
    percentage_more = Fraction(25, 100) # 25 percent more movies
    lj_productions_movies_per_year = 220 # L&J Productions produces 220 movies in a year
    johnny_tv_additional_movies = percentage_more * lj_productions_movies_per_year

    # L2
    johnny_tv_total_movies_per_year = lj_productions_movies_per_year + johnny_tv_additional_movies

    # L3
    total_movies_per_year_combined = johnny_tv_total_movies_per_year + lj_productions_movies_per_year

    # L4
    number_of_years = 5 # in five years
    total_movies_five_years = total_movies_per_year_combined * number_of_years

    # FA
    answer = total_movies_five_years
    return answer