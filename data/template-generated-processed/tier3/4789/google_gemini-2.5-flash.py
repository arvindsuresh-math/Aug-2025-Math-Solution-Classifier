def solve():
    """Index: 4789.
    Returns: the number of people Maurice can invite to the cookout.
    """
    # L1
    num_packages = 4 # purchases 4 packages of ground beef
    pounds_per_package = 5 # sells ground beef in 5-pound packages
    total_beef_pounds = num_packages * pounds_per_package

    # L2
    beef_per_burger = 2 # make one 2-pound burger
    total_burgers = total_beef_pounds / beef_per_burger

    # L3
    maurice_burgers = 1 # everybody, including himself, gets a burger
    people_invited = total_burgers - maurice_burgers

    # FA
    answer = people_invited
    return answer