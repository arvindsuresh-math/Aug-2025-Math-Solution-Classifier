from fractions import Fraction

def solve():
    """Index: 2835.
    Returns: the average number of surfers at the Festival for the three days.
    """
    # L1
    surfers_day1 = 1500 # 1500 surfers at the Festival on the first day
    additional_surfers_day2 = 600 # 600 more surfers on the second day than the first day
    surfers_day2 = surfers_day1 + additional_surfers_day2

    # L2
    fraction_day3 = Fraction(2, 5) # 2/5 as many surfers on the third day
    surfers_day3 = fraction_day3 * surfers_day1

    # L3
    total_surfers_three_days = surfers_day1 + surfers_day2 + surfers_day3

    # L4
    number_of_days = 3 # three days
    average_surfers = total_surfers_three_days / number_of_days

    # FA
    answer = average_surfers
    return answer