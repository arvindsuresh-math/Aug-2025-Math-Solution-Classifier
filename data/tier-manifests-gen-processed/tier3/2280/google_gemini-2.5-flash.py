from fractions import Fraction

def solve():
    """Index: 2280.
    Returns: the number of meters of rope left to Orlan.
    """
    # L1
    total_rope_length = 20 # 20-meter rope
    allan_fraction = Fraction(1, 4) # one-fourth of his 20-meter rope
    rope_given_to_allan = total_rope_length * allan_fraction

    # L2
    remaining_rope_after_allan = total_rope_length - rope_given_to_allan

    # L3
    jack_fraction = Fraction(2, 3) # two-thirds of the remaining
    rope_given_to_jack = remaining_rope_after_allan * jack_fraction

    # L4
    final_remaining_rope = remaining_rope_after_allan - rope_given_to_jack

    # FA
    answer = final_remaining_rope
    return answer