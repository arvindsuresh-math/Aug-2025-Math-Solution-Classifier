def solve():
    """Index: 6957.
    Returns: the total human years a 10-year-old dog has lived.
    """
    # L1
    dog_age_total = 10 # 10-year-old dog
    dog_age_year1 = 1 # first year of a dog's life
    human_years_first_year_rate = 15 # first year of a dog's life equals 15 human years
    human_years_year1 = dog_age_year1 * human_years_first_year_rate

    # L2
    dog_age_year2 = 1 # second year of a dog's life
    human_years_second_year_rate = 9 # The second year of a dog's life equals 9 human years
    human_years_year2 = dog_age_year2 * human_years_second_year_rate

    # L3
    years_accounted_for = 2 # first two years of dog's life
    remaining_dog_years = dog_age_total - years_accounted_for

    # L4
    dog_year_unit = 1 # 1 year of dog life
    human_years_subsequent_rate = 5 # every year of a dog's life equals 5 human years
    human_years_remaining = remaining_dog_years * human_years_subsequent_rate

    # L5
    total_human_years = human_years_year1 + human_years_year2 + human_years_remaining

    # FA
    answer = total_human_years
    return answer