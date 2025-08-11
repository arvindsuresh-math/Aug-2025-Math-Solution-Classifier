def solve():
    """Index: 2975.
    Returns: the number of erasers Hanna has.
    """
    # L1
    tanya_total_erasers = 20 # If Tanya has 20 erasers
    half_divisor = 2 # half of them are red
    tanya_red_erasers = tanya_total_erasers / half_divisor

    # L2
    half_of_tanya_red = tanya_red_erasers / half_divisor

    # L3
    less_than_half_amount = 3 # three less than one-half
    rachel_erasers = half_of_tanya_red - less_than_half_amount

    # L4
    hanna_multiplier = 2 # twice as many erasers
    hanna_erasers = hanna_multiplier * rachel_erasers

    # FA
    answer = hanna_erasers
    return answer