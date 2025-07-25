def solve():
    """Index: 5199.
    Returns: the difference in the number of vets recommending Yummy Dog Kibble versus Puppy Kibble.
    """
    # L1
    total_vets = 1000 # 1000 vets in the state
    puppy_kibble_percent_decimal = 0.2 # 20% of the vets
    vets_puppy_kibble = total_vets * puppy_kibble_percent_decimal

    # L2
    yummy_kibble_percent_decimal = 0.3 # 30% recommend Yummy Dog Kibble
    vets_yummy_kibble = total_vets * yummy_kibble_percent_decimal

    # L3
    difference_in_recommendations = vets_yummy_kibble - vets_puppy_kibble

    # FA
    answer = difference_in_recommendations
    return answer