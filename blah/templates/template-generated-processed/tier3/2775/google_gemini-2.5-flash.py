from fractions import Fraction

def solve():
    """Index: 2775.
    Returns: the circumference of Bill's head in inches.
    """
    # L1
    jack_head_circumference = 12 # Jack's head is 12 inches in circumference
    half_divisor = 2 # half the circumference
    half_jack_circumference = jack_head_circumference / half_divisor

    # L2
    more_than_half_jack = 9 # 9 inches more than half the circumference of Jack's head
    charlie_head_circumference = half_jack_circumference + more_than_half_jack

    # L3
    bill_fraction = Fraction(2, 3) # 2/3 the circumference of Charlie's head
    bill_head_circumference = charlie_head_circumference * bill_fraction

    # FA
    answer = bill_head_circumference
    return answer