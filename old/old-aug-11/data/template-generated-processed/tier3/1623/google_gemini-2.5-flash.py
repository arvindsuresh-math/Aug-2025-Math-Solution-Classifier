def solve():
    """Index: 1623.
    Returns: the total number of people who attended the party.
    """
    # L1
    total_women = 60 # 60 women at the party
    married_fraction_numerator = 3 # three-fourths of these women
    married_fraction_denominator = 4 # three-fourths of these women
    married_women = total_women * married_fraction_numerator / married_fraction_denominator

    # L2
    married_men = married_women # 45 married males
    married_men_fraction_denominator = 4 # 3/4 of the men at the party were single, implying 1/4 were married
    total_men = married_men_fraction_denominator * married_men

    # L3
    total_people = total_women + total_men

    # FA
    answer = total_people
    return answer