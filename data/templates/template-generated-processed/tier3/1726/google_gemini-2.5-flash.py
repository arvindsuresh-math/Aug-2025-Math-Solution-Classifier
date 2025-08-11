from fractions import Fraction

def solve():
    """Index: 1726.
    Returns: the number of non-foreign male students.
    """
    # L1
    total_students = 300 # If the school has 300 students
    female_fraction = Fraction(2, 3) # 2/3 of the population are females
    num_females = total_students * female_fraction

    # L2
    num_males = total_students - num_females

    # L3
    foreign_male_fraction = Fraction(1, 10) # One-tenth of the males are foreign students
    num_foreign_males = num_males * foreign_male_fraction

    # L4
    num_non_foreign_males = num_males - num_foreign_males

    # FA
    answer = num_non_foreign_males
    return answer