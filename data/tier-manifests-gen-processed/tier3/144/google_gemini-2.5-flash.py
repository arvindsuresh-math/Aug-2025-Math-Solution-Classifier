def solve():
    """Index: 144.
    Returns: the number of packages the third butcher delivered.
    """
    # L1
    package_weight = 4 # four-pound packages
    first_butcher_packages = 10 # first butcher delivered 10 packages
    first_butcher_weight = first_butcher_packages * package_weight

    # L2
    second_butcher_packages = 7 # 7 packages arrived from the second butcher
    second_butcher_weight = second_butcher_packages * package_weight

    # L3
    first_two_butchers_total_weight = first_butcher_weight + second_butcher_weight

    # L4
    total_ground_beef_weight = 100 # all the ground beef delivered by the three butchers weighed 100 pounds
    third_butcher_weight = total_ground_beef_weight - first_two_butchers_total_weight

    # L5
    third_butcher_packages = third_butcher_weight / package_weight

    # FA
    answer = third_butcher_packages
    return answer