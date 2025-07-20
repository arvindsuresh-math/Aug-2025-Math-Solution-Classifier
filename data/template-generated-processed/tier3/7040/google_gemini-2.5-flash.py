from fractions import Fraction

def solve():
    """Index: 7040.
    Returns: the number of dolphins that will be trained next month.
    """
    # L1
    total_dolphins = 20 # There are 20 dolphins
    trained_fraction = Fraction(1, 4) # One-fourth of the dolphins are fully trained
    fully_trained_dolphins = total_dolphins * trained_fraction

    # L2
    remaining_dolphins = total_dolphins - fully_trained_dolphins

    # L3
    in_training_fraction = Fraction(2, 3) # Two-third of the remaining dolphins are currently in training
    currently_in_training = remaining_dolphins * in_training_fraction

    # L4
    will_be_trained_next_month = remaining_dolphins - currently_in_training

    # FA
    answer = will_be_trained_next_month
    return answer