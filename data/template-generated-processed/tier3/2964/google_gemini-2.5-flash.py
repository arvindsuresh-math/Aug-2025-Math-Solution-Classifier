def solve():
    """Index: 2964.
    Returns: the age of Darcie's father.
    """
    # L1
    darcie_age = 4 # Darcie is 4 years old
    darcie_age_fraction_denominator = 6 # She is 1/6 as old as her mother
    mother_age = darcie_age * darcie_age_fraction_denominator

    # L2
    mother_father_fraction_numerator = 4 # her mother is 4/5 as old as her father
    mother_father_fraction_denominator = 5 # her mother is 4/5 as old as her father
    father_age = mother_age / mother_father_fraction_numerator * mother_father_fraction_denominator

    # FA
    answer = father_age
    return answer