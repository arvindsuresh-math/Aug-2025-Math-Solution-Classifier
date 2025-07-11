def solve():
    """Index: 2266.
    Returns: the number of additional necklaces Haley has compared to Josh.
    """
    # L1
    haley_necklaces = 25 # Haley has 25 necklaces
    haley_more_than_jason = 5 # Haley has 5 more necklaces than Jason
    jason_necklaces = haley_necklaces - haley_more_than_jason

    # L2
    josh_fraction_denominator = 2 # Josh has half the number of necklaces as Jason
    josh_necklaces = jason_necklaces / josh_fraction_denominator

    # L3
    haley_more_than_josh = haley_necklaces - josh_necklaces

    # FA
    answer = haley_more_than_josh
    return answer