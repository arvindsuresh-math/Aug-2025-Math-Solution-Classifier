from fractions import Fraction

def solve():
    """Index: 1567.
    Returns: the number of miles Billy has to run on Saturday to tie Tiffany.
    """
    # L1
    miles_per_day_billy_early = 1 # Billy runs 1 mile each day
    billy_miles_so_far = miles_per_day_billy_early + miles_per_day_billy_early + miles_per_day_billy_early + miles_per_day_billy_early + miles_per_day_billy_early + miles_per_day_billy_early

    # L2
    miles_per_day_tiffany_early = 2 # Tiffany runs 2 miles each day
    miles_per_day_tiffany_late = Fraction(1, 3) # Tiffany runs a 1/3 of a mile each day
    tiffany_miles_so_far = miles_per_day_tiffany_early + miles_per_day_tiffany_early + miles_per_day_tiffany_early + miles_per_day_tiffany_late + miles_per_day_tiffany_late + miles_per_day_tiffany_late

    # L3
    miles_billy_needs_to_run = tiffany_miles_so_far - billy_miles_so_far

    # FA
    answer = miles_billy_needs_to_run
    return answer