from fractions import Fraction

def solve():
    """Index: 7063.
    Returns: the bonus amount each female mother employee received.
    """
    # L1
    bonus_percentage = Fraction(25, 100) # 25% of Facebook's annual earnings
    annual_earnings = 5000000 # $5,000,000 for the year 2020
    total_bonus_pool = bonus_percentage * annual_earnings

    # L2
    total_employees = 3300 # 3300 employees
    male_fraction = Fraction(1, 3) # one-third are men
    male_employees = total_employees * male_fraction

    # L3
    female_employees = total_employees - male_employees

    # L4
    non_mother_women = 1200 # 1200 are not mothers
    female_mother_employees = female_employees - non_mother_women

    # L5
    bonus_per_mother = total_bonus_pool / female_mother_employees

    # FA
    answer = bonus_per_mother
    return answer