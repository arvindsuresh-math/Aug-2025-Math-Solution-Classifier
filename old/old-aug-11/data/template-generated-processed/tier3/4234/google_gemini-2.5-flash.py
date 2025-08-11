from fractions import Fraction

def solve():
    """Index: 4234.
    Returns: 5 less than 60% of the number of cats.
    """
    # L1
    hogs_count = 75 # If there are 75 hogs
    hogs_to_cats_ratio = 3 # three times as many hogs as cats
    cats_count = hogs_count / hogs_to_cats_ratio

    # L2
    percentage_value = Fraction(60, 100) # 60% of the number of cats
    sixty_percent_of_cats = percentage_value * cats_count

    # L3
    subtraction_value = 5 # 5 less than
    final_result = sixty_percent_of_cats - subtraction_value

    # FA
    answer = final_result
    return answer