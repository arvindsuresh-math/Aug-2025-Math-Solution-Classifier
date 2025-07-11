from fractions import Fraction

def solve():
    """Index: 776.
    Returns: the total hours worked by the 3 people.
    """
    # L1
    amber_hours = 12 # Amber worked for 12 hours
    armand_fraction = Fraction(1, 3) # one-third as long
    armand_hours = armand_fraction * amber_hours

    # L2
    ella_multiplier = 2 # twice as long
    ella_hours = ella_multiplier * amber_hours

    # L3
    total_hours = amber_hours + armand_hours + ella_hours

    # FA
    answer = total_hours
    return answer