def solve():
    """Index: 3685.
    Returns: the number of additional stars Luke must make.
    """
    # L1
    stars_per_jar = 85 # 85 paper stars are required to fill a glass jar
    num_bottles = 4 # he needs to fill 4 bottles
    total_stars_needed = stars_per_jar * num_bottles

    # L2
    stars_already_made = 33 # Luke has already made 33 stars
    additional_stars_needed = total_stars_needed - stars_already_made

    # FA
    answer = additional_stars_needed
    return answer