from fractions import Fraction

def solve():
    """Index: 6482.
    Returns: the total number of turtles in the lake.
    """
    # L1
    adult_percentage_striped_males = 60 # 60% are adults
    total_percentage = 100 # WK
    baby_percentage_striped_males_num = total_percentage - adult_percentage_striped_males
    baby_percentage_striped_males = baby_percentage_striped_males_num / total_percentage

    # L2
    num_baby_striped_males = 4 # 4 are babies
    total_striped_males = num_baby_striped_males / baby_percentage_striped_males

    # L3
    males_with_stripes_fraction = Fraction(1, 4) # 1 in 4 has stripes
    total_males = total_striped_males / males_with_stripes_fraction

    # L4
    female_percentage = 60 # 60% female
    male_percentage_num = total_percentage - female_percentage
    male_percentage = male_percentage_num / total_percentage

    # L5
    total_turtles = total_males / male_percentage

    # FA
    answer = total_turtles
    return answer