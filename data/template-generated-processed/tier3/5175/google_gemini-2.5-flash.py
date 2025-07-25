from fractions import Fraction

def solve():
    """Index: 5175.
    Returns: Kaydence's age.
    """
    # L1
    father_age = 60 # Kaydence's father is 60 years old
    mother_age_difference = 2 # 2 years younger than Kaydence's father
    mother_age = father_age - mother_age_difference

    # L2
    father_mother_total_age = father_age + mother_age

    # L3
    brother_age_fraction = Fraction(1, 2) # 1/2 the age of Kaydence's father
    brother_age = brother_age_fraction * father_age

    # L4
    father_mother_brother_total_age = brother_age + father_mother_total_age

    # L5
    sister_age = 40 # Kaydence's sister 40 years old
    family_members_known_total_age = father_mother_brother_total_age + sister_age

    # L6
    total_family_age = 200 # The total age of the people in Kaydence's family is 200
    kaydence_age = total_family_age - family_members_known_total_age

    # FA
    answer = kaydence_age
    return answer