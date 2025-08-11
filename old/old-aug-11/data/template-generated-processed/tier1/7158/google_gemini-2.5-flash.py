def solve():
    """Index: 7158.
    Returns: the total number of artworks the art club can collect in two school years.
    """
    # L1
    num_students = 15 # 15 students in the art club
    artworks_per_student = 2 # each student makes two artworks
    artworks_per_quarter = num_students * artworks_per_student

    # L2
    quarters_per_year = 4 # four quarters in a school year
    artworks_per_year = artworks_per_quarter * quarters_per_year

    # L3
    num_school_years = 2 # two school years
    total_artworks = artworks_per_year * num_school_years

    # FA
    answer = total_artworks
    return answer