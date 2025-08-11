from fractions import Fraction

def solve():
    """Index: 7446.
    Returns: the percentage of the school population that does not like to play basketball.
    """
    # L1
    male_ratio_part = 3 # ratio of the male to female students is 3:2
    female_ratio_part = 2 # ratio of the male to female students is 3:2
    total_ratio_parts = male_ratio_part + female_ratio_part

    # L2
    total_students = 1000 # there are 1000 students
    students_per_part = total_students / total_ratio_parts

    # L3
    num_males = male_ratio_part * students_per_part

    # L4
    num_females = female_ratio_part * students_per_part

    # L5
    male_basketball_fraction = Fraction(2, 3) # 2/3 of the male students like to play basketball
    males_play_basketball = num_males * male_basketball_fraction

    # L6
    female_basketball_fraction = Fraction(1, 5) # 1/5 of the female students like to play basketball
    females_play_basketball = num_females * female_basketball_fraction

    # L7
    total_play_basketball = males_play_basketball + females_play_basketball

    # L8
    total_not_play_basketball = total_students - total_play_basketball

    # L9
    percentage_multiplier = 100 # WK
    percent_not_play_basketball = (total_not_play_basketball / total_students) * percentage_multiplier

    # FA
    answer = percent_not_play_basketball
    return answer