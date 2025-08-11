def solve():
    """Index: 376.
    Returns: the number of more apples Suraya picked than Kayla.
    """
    # L1
    kayla_apples = 20 # If Kayla picked 20 apples
    caleb_less_than_kayla = 5 # Caleb picked 5 apples less than Kayla
    caleb_apples = kayla_apples - caleb_less_than_kayla

    # L2
    suraya_more_than_caleb = 12 # Suraya picked 12 apples more than Caleb
    suraya_apples = suraya_more_than_caleb + caleb_apples

    # L3
    difference_suraya_kayla = suraya_apples - kayla_apples

    # FA
    answer = difference_suraya_kayla
    return answer